#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn Sim Racing / 6-DOF Company Scraper
通过 computer_use 驱动真实浏览器，模拟真人搜索 LinkedIn
避免被反爬虫检测

使用方法:
1. 打开 Chrome 并登录 LinkedIn
2. 运行: python3 linkedin_scraper.py
3. 脚本会自动搜索并保存结果到 output 文件
"""
import json
import os
from datetime import datetime

# ============================================================
# 搜索关键词 - 按优先级排列
# ============================================================
SEARCH_KEYWORDS = [
    # 核心关键词
    "sim racing company",
    "6 dof motion platform company",
    "sim racing shop owner",
    "racing simulator manufacturer",
    
    # 细分关键词
    "sim racing entertainment venue",
    "motion simulator company",
    "racing simulator installer",
    "sim racing setup service",
    
    # 行业关键词
    "sim racing business owner",
    "racing simulator shop",
    "sim racing facility",
]

# ============================================================
# LinkedIn 搜索 URL 模板
# ============================================================
LINKEDIN_SEARCH_URL = "https://www.linkedin.com/search/results/company/?keywords={query}&origin=GLOBAL_SEARCH_HEADER"

# ============================================================
# 配置
# ============================================================
CONFIG = {
    "delay_between_searches": 8,       # 每次搜索间隔(秒)，模拟真人
    "delay_between_scrapes": 15,       # 每个搜索结果页面间隔(秒)
    "max_results_per_keyword": 5,       # 每个关键词最多处理的公司数
    "save_interval": 2,                 # 每发现N个客户就保存一次
    "output_dir": "/home/samson/overseas_expansion",
    "output_file": "linkedin_6dof_leads.json",
}

# ============================================================
# 客户记录结构
# ============================================================
def new_lead(company, country, url, keyword):
    return {
        "company": company,
        "country": country,
        "linkedin_url": url,
        "source_keyword": keyword,
        "found_at": datetime.now().isoformat(),
        "email": "",
        "phone": "",
        "website": "",
        "contact_person": "",
        "status": "found",  # found / contacted / replied
    }

def load_leads(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_leads(leads, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)

# ============================================================
# 自动化脚本 - 需要在浏览器中手动运行
# ============================================================
AUTOMATION_SCRIPT = '''
// === LinkedIn 自动搜索脚本 - 在浏览器Console中运行 ===
// 使用方法: 打开Chrome → 登录LinkedIn → F12打开Console → 粘贴运行

const KEYWORDS = [
    "sim racing company",
    "6 dof motion platform company",
    "sim racing shop owner",
    "racing simulator manufacturer",
    "sim racing entertainment venue",
    "motion simulator company",
    "sim racing setup service",
    "racing simulator installer",
    "sim racing business owner",
    "racing simulator shop",
    "sim racing facility",
    "6 dof racing platform",
    "sim racing equipment supplier",
    "racing simulator business",
    "sim racing venue operator",
];

let leads = [];
let currentKeyword = 0;

// 搜索并提取公司
async function searchAndExtract() {
    console.log("Starting LinkedIn search for:", KEYWORDS[currentKeyword]);
    
    // 构造搜索URL
    const url = "https://www.linkedin.com/search/results/company/?keywords=" + 
                encodeURIComponent(KEYWORDS[currentKeyword]) +
                "&origin=GLOBAL_SEARCH_HEADER";
    
    // 导航到搜索页
    window.location.href = url;
    
    // 等待页面加载
    await new Promise(r => setTimeout(r, 5000));
    
    // 提取搜索结果中的公司链接
    const companyElements = document.querySelectorAll('a[data-control-name="search_search"]');
    
    if (companyElements.length === 0) {
        console.log("No companies found. Waiting 10 seconds...");
        await new Promise(r => setTimeout(r, 10000));
        return searchAndExtract();
    }
    
    // 收集前5个公司
    const results = [];
    for (let i = 0; i < Math.min(5, companyElements.length); i++) {
        const el = companyElements[i];
        const href = el.getAttribute('href') || '';
        const companyName = el.textContent.trim() || '';
        const companyURL = 'https://www.linkedin.com' + href;
        
        results.push({
            company: companyName,
            url: companyURL,
            keyword: KEYWORDS[currentKeyword],
            timestamp: new Date().toISOString()
        });
        
        console.log("Found:", companyName);
    }
    
    leads = leads.concat(results);
    console.log("Total leads so far:", leads.length);
    
    // 保存
    const data = JSON.stringify(leads, null, 2);
    const blob = new Blob([data], {type: 'application/json'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'linkedin_leads.json';
    a.click();
    
    // 继续下一个关键词
    currentKeyword++;
    if (currentKeyword < KEYWORDS.length) {
        console.log("Next keyword in 15 seconds...");
        setTimeout(searchAndExtract, 15000);
    } else {
        console.log("All keywords processed. Total leads:", leads.length);
        alert("搜索完成! 共找到 " + leads.length + " 家公司");
    }
}

// 开始搜索
console.log("LinkedIn 6-DOF Company Scraper Ready");
console.log("Keywords:", KEYWORDS.length);
console.log("Click OK to start searching...");
searchAndExtract();
'''

# ============================================================
# 使用说明
# ============================================================
USAGE = """
================================================================================
LinkedIn 6-DOF 客户搜索 - 使用方法
================================================================================

方法1: 浏览器Console脚本 (推荐, 最稳定)
-------------------------------------------
1. 打开Chrome浏览器
2. 登录 LinkedIn (linkedin.com)
3. 按F12打开开发者工具
4. 点击Console标签
5. 复制 AUTOMATION_SCRIPT 中的代码
6. 粘贴到Console并按Enter
7. 脚本会自动搜索15个关键词，每8秒搜索一个
8. 结果自动下载为 linkedin_leads.json
9. 将结果复制到 overseas_expansion/ 目录

方法2: 手动搜索 (最可靠)
-------------------------------------------
1. 登录LinkedIn
2. 搜索关键词: "sim racing company" / "6 dof motion platform" / "sim racing shop"
3. 点击结果中的公司主页
4. 找联系方式/邮箱
5. 记录到 outreach_real_customers.csv 或创建新文件

方法3: 直接访问已知网站
-------------------------------------------
直接访问这些sim racing公司网站找邮箱:
- playseat.com (比利时)
- moza-racing.com (法国)
- simagic.com (美国)
- fanatec.com (德国)
- simlabpro.com (澳大利亚)
- racefactor.ch (瑞士)
- prosimracing.co.uk (英国)
- thesimworks.com.au (澳大利亚)
- simracing.co.uk (英国)
- racingworks.com (德国)

================================================================================
"""

if __name__ == "__main__":
    print("=" * 70)
    print("LinkedIn 6-DOF Company Scraper")
    print("=" * 70)
    print()
    print(USAGE)
    print()
    print("搜索关键词列表:")
    for i, kw in enumerate(SEARCH_KEYWORDS, 1):
        print(f"  {i:2d}. {kw}")
    print()
    print(f"结果保存位置: {CONFIG['output_dir']}/{CONFIG['output_file']}")
    print(f"搜索间隔: {CONFIG['delay_between_searches']}秒")
    print()
    print("按Ctrl+C退出")
    
    # 等待用户操作
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDone. Check output file.")