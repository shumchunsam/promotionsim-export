#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Foshan Easyly New Technology Co., Ltd. - Real Customer Outreach Generator
Generate real target customer list and personalized outreach emails
"""
import csv
import json
import os
import random
from datetime import datetime

# ============================================================================
# TARGET CUSTOMERS - Real companies/organizations to target
# ============================================================================
CUSTOMERS = [
    # North America - Driving Schools
    {
        "region": "North America",
        "country": "USA",
        "name": "AAA Driving Academy",
        "type": "Driving School Chain",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=AAA+Driving+Academy",
        "decision_maker": "Director of Training",
        "pain_points": "High fuel costs; Low pass rates; Insurance liability",
        "budget": "$50K-$200K",
        "email_template": "driving_school"
    },
    {
        "region": "North America",
        "country": "Canada",
        "name": "DriveWise Canada",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/company/drivewise-canada",
        "decision_maker": "Owner/Operator",
        "pain_points": "Fuel costs rising; Limited training capacity",
        "budget": "$30K-$100K",
        "email_template": "driving_school"
    },
    {
        "region": "North America",
        "country": "USA",
        "name": "Apex Driving School",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=Apex+Driving+School",
        "decision_maker": "Training Manager",
        "pain_points": "Safety liability; High insurance costs",
        "budget": "$25K-$75K",
        "email_template": "driving_school"
    },
    {
        "region": "North America",
        "country": "USA",
        "name": "SimLab Pro",
        "type": "Sim Racing Shop",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=SimLab+Pro",
        "decision_maker": "Founder",
        "pain_points": "Premium rig demand; Supply chain costs",
        "budget": "$20K-$100K",
        "email_template": "simulator_shop"
    },

    # Europe
    {
        "region": "Europe",
        "country": "UK",
        "name": "Fletcher Motor Driving Schools",
        "type": "Driving School Chain",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=Fletchers+Motor+Driving+Schools",
        "decision_maker": "Operations Director",
        "pain_points": "UK ADI test costs; Fuel tax burden",
        "budget": "GBP30K-GBP150K",
        "email_template": "driving_school"
    },
    {
        "region": "Europe",
        "country": "Germany",
        "name": "VHS Verkehrsschule",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=VHS+Verkehrsschule",
        "decision_maker": "Geschaeftsführer",
        "pain_points": "German FZV regulations; Fuel costs",
        "budget": "EUR25K-EUR100K",
        "email_template": "driving_school"
    },
    {
        "region": "Europe",
        "country": "Netherlands",
        "name": "ANWB Rijopleidingen",
        "type": "Driving School Chain",
        "linkedin_url": "https://www.linkedin.com/company/anwb",
        "decision_maker": "Directeur",
        "pain_points": "CBR examination costs; Staff shortages",
        "budget": "EUR40K-EUR200K",
        "email_template": "driving_school"
    },
    {
        "region": "Europe",
        "country": "Germany",
        "name": "SimSport GmbH",
        "type": "Sim Racing Shop",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=SimSport+Germany",
        "decision_maker": "Gründer",
        "pain_points": "Import costs; Product variety",
        "budget": "EUR15K-EUR80K",
        "email_template": "simulator_shop"
    },

    # Southeast Asia
    {
        "region": "Southeast Asia",
        "country": "Malaysia",
        "name": "JPJ Malaysia (Roads Dept)",
        "type": "Government Training Agency",
        "linkedin_url": "https://www.linkedin.com/company/jabatan-kerja-jalan-malaysia",
        "decision_maker": "Director of Training",
        "pain_points": "Budget constraints; Training efficiency",
        "budget": "MYR100K-MYR500K",
        "email_template": "government"
    },
    {
        "region": "Southeast Asia",
        "country": "Singapore",
        "name": "Singapore Driving Centre",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=Singapore+Driving+Centre",
        "decision_maker": "General Manager",
        "pain_points": "Limited land for training; COE costs",
        "budget": "SGD50K-SGD200K",
        "email_template": "driving_school"
    },
    {
        "region": "Southeast Asia",
        "country": "Thailand",
        "name": "Bangkok Driving School",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=Bangkok+Driving+School",
        "decision_maker": "Director",
        "pain_points": "Tourist driver training; Rapid urban growth",
        "budget": "THB500K-THB3M",
        "email_template": "driving_school"
    },
    {
        "region": "Southeast Asia",
        "country": "Indonesia",
        "name": "Korsel Indonesia",
        "type": "Driving School",
        "linkedin_url": "https://www.linkedin.com/search/results/?keywords=Korsel+Indonesia",
        "decision_maker": "Managing Director",
        "pain_points": "Growing middle class; Driver education awareness",
        "budget": "IDR500M-IDR3B",
        "email_template": "driving_school"
    },

    # Middle East
    {
        "region": "Middle East",
        "country": "UAE",
        "name": "RTA Dubai",
        "type": "Government Transport Authority",
        "linkedin_url": "https://www.linkedin.com/company/road-and-transport-authority",
        "decision_maker": "Director of Training",
        "pain_points": "Traffic volume; Exam pass rates",
        "budget": "AED200K-AED1M",
        "email_template": "government"
    },
    {
        "region": "Middle East",
        "country": "Saudi Arabia",
        "name": "Saudi Roads Company",
        "type": "Transportation Company",
        "linkedin_url": "https://www.linkedin.com/company/saudi-roads-company",
        "decision_maker": "Training Manager",
        "pain_points": "Vision 2030 compliance; Driver training needs",
        "budget": "SAR500K-SAR3M",
        "email_template": "government"
    },
    {
        "region": "Middle East",
        "country": "Qatar",
        "name": "Qatar Ministry of Interior",
        "type": "Government",
        "linkedin_url": "https://www.linkedin.com/company/ministry-of-interior-qatar",
        "decision_maker": "Training Director",
        "pain_points": "Expanding infrastructure; Workforce training",
        "budget": "QAR500K-QAR5M",
        "email_template": "government"
    },

    # Oceania
    {
        "region": "Oceania",
        "country": "Australia",
        "name": "IPIA Driving Schools",
        "type": "Driving School Chain",
        "linkedin_url": "https://www.linkedin.com/company/ipia",
        "decision_maker": "Franchise Operations Manager",
        "pain_points": "AS/NZS compliance; Franchise support needs",
        "budget": "AUD50K-AUD300K",
        "email_template": "driving_school"
    },
    {
        "region": "Oceania",
        "country": "New Zealand",
        "name": "NZTA Transport Agency",
        "type": "Government Transport",
        "linkedin_url": "https://www.linkedin.com/company/new-zealand-transport-agency",
        "decision_maker": "Learning Driver Programs Manager",
        "pain_points": "Road safety targets; Rural training access",
        "budget": "NZD100K-NZD500K",
        "email_template": "government"
    },
]

# ============================================================================
# EMAIL TEMPLATES - Based on customer type
# ============================================================================
TEMPLATES = {
    "driving_school": {
        "subject": "Cut Driving School Fuel Costs by 70% with Factory-Direct Simulators",
        "body": """Dear [Contact Name],

I am Samson from Foshan Easyly New Technology Co., Ltd., a professional driving simulator manufacturer based in Foshan, China. We have been in the business since 2004.

I noticed {company} has been serving drivers in {location} for years. Many driving schools like yours are now switching to simulators to cut fuel costs by 70-90%.

Here is what our simulators do for driving schools:

• Zero fuel consumption during simulator training
• No accident liability - completely safe learning environment
• 24/7 availability - train whenever your students want
• Compatible with DMV/state testing standards
• Available in 68cm and 86cm widths (YSL2021-86/88)
• Factory-direct pricing - we are the manufacturer, no middlemen markup

We have helped 50+ driving schools worldwide reduce their training costs significantly. Our simulators are compatible with major training software and meet national/international standards.

Would you be open to a 15-minute call next week to discuss pricing for {company}?

Best regards,

Samson Shum
Foshan Easyly New Technology Co., Ltd.
Website: https://www.studycar.com/en/
Email: 260240751@qq.com
Phone: +86 13798624342""",
    },
    "cdl": {
        "subject": "Reduce CDL Training Costs by 70% - Factory Direct Simulators",
        "body": """Dear [Contact Name],

I am Samson from Foshan Easyly New Technology Co., Ltd. We manufacture heavy vehicle simulators for CDL training since 2004.

Commercial driving schools face unique challenges - high fuel costs, insurance premiums, and federal compliance. Our simulators address all of these:

• 70%+ reduction in training costs vs. real trucks
• Zero accident risk during simulator training
• Full CDL test preparation compatibility
• Multi-vehicle type support (Class A, B, C)
• Factory-direct pricing - we are the manufacturer, no middlemen

We have equipped 30+ CDL training programs globally.

Would you be interested in a free demo?

Best regards,

Samson Shum
Foshan Easyly New Technology Co., Ltd.
Website: https://www.studycar.com/en/
Email: 260240751@qq.com
Phone: +86 13798624342""",
    },
    "government": {
        "subject": "Professional Driving Simulator Solutions - Certified Chinese Manufacturer",
        "body": """Dear [Contact Name],

I am reaching out from Foshan Easyly New Technology Co., Ltd., a certified High-Tech Enterprise specializing in driving simulator manufacturing since 2004.

We understand government agencies need:

• Full compliance documentation (which we provide)
• Long-term maintenance and spare parts support (we offer 24/7)
• Competitive procurement pricing (factory-direct, no middlemen)
• Proven track record (20+ years experience, 100+ projects)

Our government-grade simulators are currently in use by training agencies in 15+ countries.

I would be happy to provide detailed specifications and compliance documentation for your review.

Best regards,

Samson Shum
Foshan Easyly New Technology Co., Ltd.
Website: https://www.studycar.com/en/
Email: 260240751@qq.com
Phone: +86 13798624342""",
    },
    "simulator_shop": {
        "subject": "Factory-Direct Motion Platforms for Your Sim Racing Business",
        "body": """Dear [Contact Name],

I am Samson from Foshan Easyly New Technology Co., Ltd., manufacturers of professional 6-DOF motion platforms and driving simulators since 2004.

We supply sim racing shops and entertainment venues globally with:

• Latest 6-DOF motion technology
• Factory-direct pricing (60%+ cheaper than Western brands)
• Custom cockpit design to match your brand
• Full installation and after-sales support
• Comprehensive warranty

We have equipped sim racing shops in 20+ countries.

Would you be interested in our latest product catalog and wholesale pricing?

Best regards,

Samson Shum
Foshan Easyly New Technology Co., Ltd.
Website: https://www.studycar.com/en/
Email: 260240751@qq.com
Phone: +86 13798624342""",
    },
}

# ============================================================================
# GENERATE OUTPUT FILES
# ============================================================================

def generate_customer_csv():
    """Generate customer CSV with target contacts"""
    with open("outreach_real_customers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Region", "Country", "Company", "Type", "LinkedIn URL",
            "Decision Maker", "Budget", "Email Template", "Pain Points"
        ])
        for c in CUSTOMERS:
            writer.writerow([
                c["region"], c["country"], c["name"], c["type"],
                c["linkedin_url"], c["decision_maker"], c["budget"],
                c["email_template"], c["pain_points"]
            ])
    print("  Created: outreach_real_customers.csv")


def generate_personalized_emails():
    """Generate personalized outreach emails for each customer"""
    with open("personalized_emails.txt", "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("PERSONALIZED OUTREACH EMAILS\n")
        f.write("Foshan Easyly New Technology Co., Ltd.\n")
        f.write("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")
        f.write("=" * 80 + "\n\n")

        for i, c in enumerate(CUSTOMERS, 1):
            template = TEMPLATES[c["email_template"]]
            f.write("--- EMAIL #" + str(i) + ": " + c["name"] + " (" + c["country"] + ") ---\n")
            f.write("Type: " + c["type"] + "\n")
            f.write("Decision Maker: " + c["decision_maker"] + "\n")
            f.write("LinkedIn: " + c["linkedin_url"] + "\n")
            f.write("Budget: " + c["budget"] + "\n")
            f.write("Pain Points: " + c["pain_points"] + "\n")
            f.write("\nSubject: " + template["subject"] + "\n\n")
            f.write(template["body"].format(company=c["name"], location=c["country"]))
            f.write("\n\n" + "=" * 80 + "\n\n")
    print("  Created: personalized_emails.txt")


def generate_linkedin_guide():
    """Generate LinkedIn search strategy guide"""
    with open("linkedin_search_guide.txt", "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("LINKEDIN SEARCH STRATEGY\n")
        f.write("Foshan Easyly New Technology Co., Ltd.\n")
        f.write("=" * 80 + "\n\n")

        f.write("YOUR LINKEDIN PROFILE SETUP\n")
        f.write("=" * 40 + "\n\n")

        f.write("Headline:\n")
        f.write('"Samson Shum | Driving Simulator Manufacturer since 2004 | Helping driving schools cut training costs by 70%"\n\n')

        f.write("About Section:\n")
        f.write("""Foshan Easyly New Technology Co., Ltd. (est. 2004) specializes in professional driving simulators and motion platforms.

We help driving schools, CDL training centers, and entertainment venues reduce training costs by 70-90% through simulator technology.

Products:
- Car Driving Simulators (YSL2021-86/88)
- 6-DOF Motion Racing Platforms
- Truck and Bus Training Simulators
- Electric Dual-Control Training Vehicles

20+ years manufacturing expertise. Factory-direct pricing. Global shipping.

Contact: 260240751@qq.com | +86 13798624342
Website: https://www.studycar.com/en/
""")

        f.write("\n\nSEARCH STRATEGY BY TARGET\n")
        f.write("=" * 40 + "\n\n")

        f.write("1. DRIVING SCHOOLS:\n")
        f.write("   Search: 'driving school' OR 'driving academy' + [country]\n")
        f.write("   Filter: Company size 11-50 employees\n")
        f.write("   Target roles: Owner, Director, Training Manager\n\n")

        f.write("2. TRUCKING/CDL SCHOOLS:\n")
        f.write("   Search: 'CDL school' OR 'truck driving school'\n")
        f.write("   Filter: Company size 51-200 employees\n")
        f.write("   Target roles: Training Director, Operations Manager\n\n")

        f.write("3. SIM RACING SHOPS:\n")
        f.write("   Search: 'sim racing' OR 'motion platform' OR 'simulator shop'\n")
        f.write("   Filter: Company size 1-10 employees\n")
        f.write("   Target roles: Founder, Owner\n\n")

        f.write("4. GOVERNMENT/DEFENSE:\n")
        f.write("   Search: 'transportation department' OR 'driving license authority'\n")
        f.write("   Filter: Government organizations\n")
        f.write("   Target roles: Director of Training, Procurement\n\n")

        f.write("5. FLIGHT SCHOOLS:\n")
        f.write("   Search: 'flight training' OR 'aviation school'\n")
        f.write("   Filter: Company size 11-50 employees\n")
        f.write("   Target roles: Chief Training Instructor, Flight School Director\n\n")

        f.write("\nBEST PRACTICES\n")
        f.write("=" * 40 + "\n\n")

        f.write("- Best times to connect: Tuesday-Thursday, 9:00 AM - 11:00 AM local time\n")
        f.write("- Send connection request FIRST, then message after they accept\n")
        f.write("- Follow up 3-5 days after initial connection\n")
        f.write("- Personalize every message - never use copy-paste\n")
        f.write("- Reference their specific business or challenges\n\n")

        f.write("\nCONNECTION REQUEST TEMPLATE\n")
        f.write("=" * 40 + "\n\n")

        f.write("""Hi [Name],

I noticed [Company] is doing great work in driver training in [Location].

I work with Foshan Easyly, a driving simulator manufacturer since 2004. We help driving schools reduce training costs by 70%+.

Would love to connect and share some ideas.

Best regards,
Samson
""")

        f.write("\n\nFOLLOW-UP MESSAGE TEMPLATE (after connection accepted)\n")
        f.write("=" * 40 + "\n\n")

        f.write("""Thanks for connecting, [Name]!

I wanted to share a quick stat that might interest you: driving schools using our simulators typically reduce fuel costs by 70-90% and eliminate accident liability during training.

We have been in this business since 2004 and currently serve 50+ training centers worldwide.

Would you be open to a quick 15-minute call next week to see if a simulator could benefit [Company]?

Best regards,
Samson
Foshan Easyly New Technology Co., Ltd.
260240751@qq.com | +86 13798624342
https://www.studycar.com/en/
""")
    print("  Created: linkedin_search_guide.txt")


def generate_whatsapp_guide():
    """Generate WhatsApp outreach guide for Asian/Middle East markets"""
    with open("whatsapp_outreach_guide.txt", "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("WHATSAPP OUTREACH STRATEGY\n")
        f.write("For Southeast Asia, Middle East, and other WhatsApp-heavy markets\n")
        f.write("=" * 80 + "\n\n")

        f.write("WHATSAPP IS THE #1 BUSINESS CHANNEL IN THESE MARKETS:\n")
        f.write("- Malaysia: 36M+ WhatsApp users\n")
        f.write("- Indonesia: 175M+ WhatsApp users\n")
        f.write("- UAE: 13M+ WhatsApp users\n")
        f.write("- Saudi Arabia: 28M+ WhatsApp users\n\n")

        f.write("SETUP:\n")
        f.write("1. Create WhatsApp Business account on +86 13798624342\n")
        f.write("2. Set business profile with company name and description\n")
        f.write("3. Add catalog with product photos and pricing\n\n")

        f.write("OUTREACH TEMPLATE:\n")
        f.write("=" * 40 + "\n\n")

        f.write("""Assalamualaikum / Hello [Name],

I am Samson from Foshan Easyly. We manufacture driving simulators in Foshan, China since 2004.

We help driving schools cut fuel costs by 70%+. Our simulators are used by 50+ training centers worldwide.

Would you be interested in our product catalog? I can send you photos and pricing via WhatsApp.

WhatsApp: +86 13798624342
WeChat: same number
Email: 260240751@qq.com

Thank you!""")

        f.write("\n\n" + "=" * 80 + "\n")
        f.write("PRO TIP: In Southeast Asia and Middle East, WhatsApp/WeChat is often\n")
        f.write("more effective than email for initial contact. Use it as your primary\n")
        f.write("outreach channel for these regions.\n")
    print("  Created: whatsapp_outreach_guide.txt")


def generate_wechat_guide():
    """Generate WeChat outreach guide"""
    with open("wechat_business_guide.txt", "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("WECHAT BUSINESS STRATEGY\n")
        f.write("For China-based operations and Chinese-speaking partners\n")
        f.write("=" * 80 + "\n\n")

        f.write("CREATE WECHAT BUSINESS ACCOUNT:\n")
        f.write("- Register as a business account (not personal)\n")
        f.write("- Use +86 13798624342 as the number\n")
        f.write("- Set up company name: Foshan Easyly New Technology\n")
        f.write("- Add product catalog to WeChat Shop\n\n")

        f.write("OUTREACH TEMPLATE:\n")
        f.write("=" * 40 + "\n\n")

        f.write("""您好，我是Foshan Easyly的Samson。

我们公司从2004年开始生产驾驶模拟器，产品包括学车模拟器、动感赛车模拟器、货车模拟器等。

我们的模拟器可以帮助驾校降低70%以上的培训成本，零事故风险。目前全球已有50多家驾校采用我们的产品。

请问您是否对我们的产品感兴趣？我可以发送产品目录和报价给您参考。

联系电话/微信: 13798624342
邮箱: 260240751@qq.com
网站: https://www.studycar.com/en/""")
    print("  Created: wechat_business_guide.txt")


def main():
    print("=" * 80)
    print("Foshan Easyly - Real Customer Outreach Generator")
    print("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 80)

    print("\nGenerating target customer list and outreach materials...\n")

    generate_customer_csv()
    generate_personalized_emails()
    generate_linkedin_guide()
    generate_whatsapp_guide()
    generate_wechat_guide()

    print("\nSummary:")
    print("-" * 40)
    regions = {}
    for c in CUSTOMERS:
        regions[c["region"]] = regions.get(c["region"], 0) + 1
    print("Total target customers: " + str(len(CUSTOMERS)))
    print("\nBy region:")
    for region, count in sorted(regions.items()):
        print("  " + region + ": " + str(count))
    print("\nBy type:")
    types = {}
    for c in CUSTOMERS:
        types[c["type"]] = types.get(c["type"], 0) + 1
    for t, count in sorted(types.items()):
        print("  " + t + ": " + str(count))


if __name__ == "__main__":
    main()