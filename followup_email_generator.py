#!/usr/bin/env python3
"""
Follow-up Email Generator
自动生成跟进邮件 (第3天/第7天/第14天)
"""

import csv
import os
from datetime import datetime, timedelta


def load_customers(csv_path="outreach_real_customers.csv"):
    """加载客户数据"""
    customers = []
    csv_file = os.path.join(os.path.dirname(__file__), csv_path)
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(row)
    return customers


def generate_followup_sequence(customer, days_late=3):
    """生成跟进邮件序列"""
    name = customer.get("Company", "your company")
    region = customer.get("Region", "your region")
    contact = customer.get("Contact", "")
    industry = customer.get("Industry", "driving training")
    
    # 第3天跟进
    day3 = f"""Hi [Contact Name],

Just checking if you had a chance to review my previous email about our driving simulators.

We have helped {name} and other driving schools in {region} reduce fuel costs by 70-90%. I would be happy to share some case studies if you are interested.

Also, our simulators are compatible with [specific training software in your country], so integration would be seamless.

Would you like me to send you our product catalog?

Best regards,
Samson Shum
Foshan Easyly New Technology Co., Ltd.
Email: 260240751@qq.com
Phone: +86 13798624342
Website: https://www.studycar.com/en/"""

    # 第7天跟进
    day7 = f"""Hi [Contact Name],

I wanted to share a quick success story from a driving school in {region} who switched to our simulators:

• Before: $2,500/month on fuel and maintenance
• After: $350/month on simulator maintenance
• Annual savings: $26,100
• ROI achieved in 4 months

Our customers consistently report:
• 70%+ cost reduction
• 40% faster training completion
• Zero accident liability
• Higher student pass rates

Are you open to a 15-minute call this week? I can show you simulators in action via video call.

Best regards,
Samson Shum
Foshan Easyly New Technology Co., Ltd.
Email: 260240751@qq.com
Phone: +86 13798624342
Website: https://www.studycar.com/en/"""

    # 第14天跟进 (最后跟进)
    day14 = f"""Hi [Contact Name],

This is my final follow-up regarding our driving simulators.

If you are not the right person to speak with about training equipment at {name}, could you please point me in the right direction?

Either way, thank you for your time. I hope to work with {name} in the future.

If you decide to explore simulator technology later, feel free to reach out anytime. We are always happy to provide information.

Best regards,
Samson Shum
Foshan Easyly New Technology Co., Ltd.
Email: 260240751@qq.com
Phone: +86 13798624342
Website: https://www.studycar.com/en/

P.S. We offer a special promotion for early adopters this month: FREE shipping + 3-year warranty. Let me know if you would like details.
"""

    return {
        "day3": day3,
        "day7": day7,
        "day14": day14,
    }


def main():
    """主函数"""
    print("=" * 80)
    print("Foshan Easyly - Follow-up Email Generator")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 80)
    
    customers = load_customers()
    
    if not customers:
        print("ERROR: No customers found in outreach_real_customers.csv")
        return
    
    output_file = "followup_emails.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Foshan Easyly - Follow-up Email Sequence\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Total Customers: {len(customers)}\n")
        f.write("=" * 80 + "\n\n")
        
        for i, customer in enumerate(customers, 1):
            name = customer.get("Company", "your company")
            region = customer.get("Region", "your region")
            contact = customer.get("Contact", "")
            industry = customer.get("Industry", "driving training")
            
            f.write(f"\n{'='*80}\n")
            f.write(f"Customer #{i}: {name}\n")
            f.write(f"Region: {region}\n")
            f.write(f"Industry: {industry}\n")
            f.write(f"Contact: {contact}\n")
            f.write(f"{'='*80}\n\n")
            
            sequences = generate_followup_sequence(customer)
            
            f.write(f"--- DAY 3 FOLLOW-UP (发送于第3天) ---\n")
            f.write(sequences["day3"])
            f.write(f"\n\n{'='*80}\n\n")
            
            f.write(f"--- DAY 7 FOLLOW-UP (发送于第7天) ---\n")
            f.write(sequences["day7"])
            f.write(f"\n\n{'='*80}\n\n")
            
            f.write(f"--- DAY 14 FOLLOW-UP (发送于第14天，最后跟进) ---\n")
            f.write(sequences["day14"])
            f.write(f"\n\n{'='*80}\n\n")
    
    print(f"\nGenerated follow-up emails for {len(customers)} customers")
    print(f"Output saved to: {output_file}")
    
    # 打印示例
    customer = customers[0]
    print(f"\n--- Example: {customer.get('Company')} ---")
    print("Follow-up sequence for this customer has been generated.")
    print(f"Region: {customer.get('Region')}")
    print(f"Industry: {customer.get('Industry')}")


if __name__ == "__main__":
    main()