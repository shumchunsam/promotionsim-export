#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMTP 握手验证 - 发信前验证邮箱是否真实存在

原理:
1. DNS 查询 MX 记录，找到对方的邮件服务器
2. SMTP EHLO 握手，确认对方邮件服务器在线
3. 尝试 RCPT TO: 命令，看对方是否接受该邮箱
4. 如果对方接受，邮箱真实存在；如果拒绝，邮箱不存在

注意: 有些邮件服务器会拒绝 RCPT TO 查询（反垃圾邮件策略），
      但能通过的邮箱基本确定是真实的。

使用:
    python3 verify_email.py user@example.com
    python3 verify_email.py batch.csv
    python3 verify_email.py --list
"""

import smtplib
import subprocess
import re
import sys
import csv
import time
import json
from datetime import datetime
from collections import namedtuple


def get_mx_records(domain):
    """查询域名的 MX 记录，使用 nslookup 或 dig"""
    
    # 尝试用 dig 查询
    try:
        result = subprocess.run(
            ['dig', 'MX', '+short', domain],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            mx_list = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    parts = line.split()
                    priority = int(parts[0])
                    server = parts[1].rstrip('.')
                    mx_list.append((priority, server))
            mx_list.sort()
            return [m[1] for m in mx_list]
    except FileNotFoundError:
        pass
    
    # 尝试用 nslookup 查询
    try:
        result = subprocess.run(
            ['nslookup', '-type=MX', domain],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            mx_list = []
            for line in result.stdout.split('\n'):
                line = line.strip()
                # 匹配: example.com mail is handled by 10 mail.example.com
                match = re.search(r'mail is handled by (\d+) (.+)', line)
                if match:
                    priority = int(match.group(1))
                    server = match.group(2).rstrip('.')
                    mx_list.append((priority, server))
                # 匹配: server: mail.example.com (after MX lookup)
                elif line.startswith('mail') and 'handled' not in line:
                    parts = line.split()
                    for i, p in enumerate(parts):
                        if p == 'handled' and i+2 < len(parts):
                            try:
                                priority = int(parts[i-1])
                                server = parts[i+2].rstrip('.')
                                mx_list.append((priority, server))
                            except ValueError:
                                pass
            mx_list.sort()
            return [m[1] for m in mx_list]
    except FileNotFoundError:
        pass
    
    return []


def verify_email_smtp(email, timeout=10):
    """通过 SMTP 握手验证邮箱是否真实存在"""
    
    # 1. 解析邮箱域名
    domain = email.split('@')[1].lower()
    
    print(f"  [1/3] 查询 MX 记录: {domain}")
    mx_servers = get_mx_records(domain)
    if not mx_servers:
        return 'FAIL', "无 MX 记录，域名不存在"
    
    print(f"  [2/3] 邮件服务器: {mx_servers[0]}")
    
    # 2. SMTP 握手
    try:
        server = smtplib.SMTP(timeout=timeout)
        server.connect(mx_servers[0], 25)
        server.ehlo('easyly-simulator.com')
        print(f"  [2/3] EHLO 响应: {server.ehlo_resp.decode()[:50]}...")
    except Exception as e:
        return 'UNVERIFIED', f"SMTP 连接失败: {e}"
    
    # 3. 尝试 RCPT TO
    try:
        from_address = 'verify@easyly-simulator.com'
        server.mail(from_address)
        code, message = server.rcpt(email)
        server.quit()
        
        if code == 250:
            return 'VALID', "邮箱存在 (SMTP 接受)"
        elif code == 550:
            return 'INVALID', f"邮箱不存在 (550 拒绝)"
        elif code == 450:
            return 'UNVERIFIED', f"暂时不可用 (450，服务器繁忙或限流)"
        else:
            return 'UNVERIFIED', f"未知响应码: {code} - {message.decode()[:50]}"
    except smtplib.SMTPRecipientsRefused as e:
        return 'INVALID', f"被拒绝: {e.recipients}"
    except Exception as e:
        return 'UNVERIFIED', f"验证异常: {e}"


def verify_email_list(emails):
    """批量验证邮箱列表"""
    results = []
    
    print("="*70)
    print(f"开始验证 {len(emails)} 个邮箱")
    print("="*70)
    
    for i, email in enumerate(emails, 1):
        email = email.strip()
        if not email or '@' not in email:
            continue
            
        print(f"\n[{i}/{len(emails)}] 验证: {email}")
        
        status, message = verify_email_smtp(email)
        
        # 颜色标记
        color = {
            'VALID': '\033[92m',      # 绿色
            'INVALID': '\033[91m',    # 红色
            'UNVERIFIED': '\033[93m', # 黄色
        }
        reset = '\033[0m'
        
        print(f"  [{color.get(status, '')}{status}{reset}] {message}")
        
        results.append({
            'email': email,
            'status': status,
            'message': message,
            'timestamp': datetime.now().isoformat(),
        })
        
        # 每次验证间隔 3 秒，避免被封
        if i < len(emails):
            time.sleep(3)
    
    # 统计
    valid = sum(1 for r in results if r['status'] == 'VALID')
    invalid = sum(1 for r in results if r['status'] == 'INVALID')
    unverified = sum(1 for r in results if r['status'] == 'UNVERIFIED')
    
    print("\n" + "="*70)
    print("验证结果汇总:")
    print(f"  有效邮箱: {valid}")
    print(f"  无效邮箱: {invalid}")
    print(f"  无法验证: {unverified}")
    print("="*70)
    
    return results


def load_emails_from_csv(filepath):
    """从 CSV 文件加载邮箱列表"""
    emails = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'email' in row and row['email']:
                emails.append(row['email'])
    return emails


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 verify_email.py <email>")
        print("  python3 verify_email.py batch.csv")
        print("  python3 verify_email.py --list")
        sys.exit(1)
    
    arg = sys.argv[1]
    
    if arg == '--list':
        # 显示已有的客户邮箱列表
        csv_files = [
            '/home/samson/overseas_expansion/engineering_simulator_customers.csv',
            '/home/samson/overseas_expansion/outreach_real_customers.csv',
        ]
        all_emails = []
        for csv_file in csv_files:
            try:
                emails = load_emails_from_csv(csv_file)
                print(f"\n来自 {csv_file}:")
                for email in emails:
                    print(f"  {email}")
                all_emails.extend(emails)
            except FileNotFoundError:
                print(f"{csv_file} 不存在")
        print(f"\n总计: {len(all_emails)} 个邮箱")
        print(f"\n验证命令: python3 verify_email.py batch.csv")
        return
    
    # 批量验证
    if arg.endswith('.csv'):
        emails = load_emails_from_csv(arg)
    else:
        emails = [arg]
    
    results = verify_email_list(emails)
    
    # 保存验证结果
    log_file = '/home/samson/overseas_expansion/email_verification_log.json'
    log_data = {
        'timestamp': datetime.now().isoformat(),
        'total': len(results),
        'valid': sum(1 for r in results if r['status'] == 'VALID'),
        'invalid': sum(1 for r in results if r['status'] == 'INVALID'),
        'results': results,
    }
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
    print(f"\n结果已保存到 {log_file}")


if __name__ == '__main__':
    main()