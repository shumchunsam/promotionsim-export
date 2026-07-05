# -*- coding: utf-8 -*-
"""
Foshan Easyly - Social Media Scheduler
Automated 30-day content calendar for driving simulator export marketing
"""

import json
import os
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

COMPANY = {
    "name": "Foshan Easyly New Technology Co., Ltd.",
    "name_short": "Easyly",
    "founded": 2004,
    "location": "Foshan, Guangdong, China",
    "website": "https://www.studycar.com",
    "website_en": "https://www.studycar.com/en/",
    "email": "260240751@qq.com",
    "phone": "+86 13798624342"
}

PRODUCTS = {
    "driving_simulator": {"name": "Car Driving Simulator", "emoji": "[CAR]", "industry": "Driving Training", "model": "YSL2021-86/88"},
    "racing_simulator": {"name": "6-DOF Racing Simulator", "emoji": "[RACE]", "industry": "Sim Racing", "model": "6-DOF Motion Platform"},
    "heavy_vehicle": {"name": "Truck & Bus Simulator", "emoji": "[BUS]", "industry": "Commercial Driving", "model": "Heavy Vehicle Series"},
    "electric_vehicle": {"name": "Electric Training Vehicle", "emoji": "[EV]", "industry": "New Energy Training", "model": "Dual-Control EV Series"}
}

CONTENT_TYPES = {
    "product_showcase": {"title": "Product Showcase", "platforms": ["LinkedIn", "Instagram", "YouTube"]},
    "customer_story": {"title": "Customer Success Story", "platforms": ["LinkedIn", "Facebook"]},
    "technical_insight": {"title": "Technical Insight", "platforms": ["LinkedIn", "YouTube"]},
    "behind_the_scenes": {"title": "Behind the Scenes", "platforms": ["Instagram", "TikTok", "YouTube Shorts"]},
    "industry_news": {"title": "Industry News", "platforms": ["LinkedIn", "Twitter"]},
    "educational": {"title": "Educational Content", "platforms": ["Facebook", "YouTube", "LinkedIn"]},
    "testimonial": {"title": "Testimonial", "platforms": ["LinkedIn", "Facebook", "YouTube"]},
    "promotional": {"title": "Promotional", "platforms": ["Instagram", "Facebook", "LinkedIn"]}
}

PLATFORM_CONFIG = {
    "LinkedIn": {"max_characters": 3000, "best_posting_times": ["Tuesday 10:00 AM", "Wednesday 9:00 AM", "Thursday 11:00 AM"], "hashtag_limit": 5, "tone": "Professional, B2B-focused", "image_ratio": "1200x627px"},
    "Instagram": {"max_characters": 2200, "best_posting_times": ["Monday-Friday 11:00 AM-1:00 PM", "Saturday 10:00 AM-11:00 AM"], "hashtag_limit": 30, "tone": "Visual, engaging", "image_ratio": "1:1 or 4:5"},
    "YouTube": {"max_characters": 5000, "best_posting_times": ["Monday-Wednesday 2:00-4:00 PM", "Friday 1:00-3:00 PM"], "hashtag_limit": 15, "tone": "Informative, high-quality production", "image_ratio": "16:9 thumbnails"},
    "Facebook": {"max_characters": 63206, "best_posting_times": ["Monday-Friday 1:00-3:00 PM", "Saturday 9:00-11:00 AM"], "hashtag_limit": None, "tone": "Community-focused", "image_ratio": "1200x630px"},
    "TikTok": {"max_characters": 2200, "best_posting_times": ["Monday-Friday 6:00-10:00 AM", "12:00-1:00 PM", "7:00-11:00 PM"], "hashtag_limit": None, "tone": "Casual, trending", "image_ratio": "9:16 vertical"}
}

def generate_hashtags(content_type, product, region="global"):
    base = {
        "driving_simulator": ["#drivingsimulator", "#drivingtraining", "#drivertraining", "#simracing", "#easyly"],
        "racing_simulator": ["#racing simulator", "#6dof", "#simracing", "#motionplatform", "#easyly"],
        "heavy_vehicle": ["#truckdriver", "#commercialdriving", "#CDLtraining", "#busdriving"],
        "electric_vehicle": ["#electricvehicle", "#evtraining", "#newenergy", "#dualcontrol"]
    }
    regional = {
        "north_america": ["#USAdriving", "#CanadaTraining"],
        "europe": ["#EuroDriving", "#UKTraining", "#GermanDriving"],
        "southeast_asia": ["#ThaiDriving", "#SGTraining"],
        "middle_east": ["#UAEDriving", "#SaudiTraining"],
        "oceania": ["#AusDriving"]
    }
    trending = [str(datetime.now().year), "#immersivelearning", "#safetytraining", "#manufacturing"]
    hashtags = base.get(product, []) + regional.get(region, []) + trending
    return list(set(hashtags))

def generate_post_content(content_type, product, region, platform):
    pi = PRODUCTS[product]
    pc = PLATFORM_CONFIG[platform]
    hashtags = generate_hashtags(content_type, product, region)
    
    posts = {
        "product_showcase": {
            "title": pi["name"] + " - Precision Engineering Since 2004",
            "body": pi["emoji"] + " Introducing our " + pi["name"] + " (" + pi["model"] + ") by Foshan Easyly.\n\nFactory-direct driving simulators trusted worldwide since 2004.\n\nKey Features:\n- Professional-grade motion system\n- Custom cockpit configurations\n- Compatible with all major training software\n- Factory-direct pricing (no middlemen)\n- Global shipping and installation\n- 20+ years manufacturing experience\n\nPerfect for driving schools, CDL centers, sim racing enthusiasts.\n\nVisit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "customer_story": {
            "title": "Customer Success: Training Centers Trust Easyly",
            "body": "Real Results from Real Customers:\n\nDriving schools using Easyly simulators report:\n- 70-90% reduction in training costs vs real vehicles\n- 40% improvement in training efficiency\n- Zero safety incidents during simulator training\n- 25% increase in student throughput\n\nSince 2004, Easyly has been the trusted choice.\n\nVisit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "technical_insight": {
            "title": "Technical Deep Dive: How Driving Simulators Work",
            "body": "Understanding " + pi["name"] + " Technology\n\nAt Foshan Easyly (est. 2004), we engineer simulators that replicate real driving:\n\nMotion Systems:\n- 3DOF: Pitch, Roll, Yaw\n- 6DOF: Full motion with Heave, Surge, Sway\n\nKey Components:\n- Professional-grade actuators\n- Real-time control algorithms\n- Multi-monitor display integration\n- Custom-tuned motion profiles\n\nVisit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "behind_the_scenes": {
            "title": "Inside Easyly: How We Build Simulators",
            "body": "Behind the Scenes: Simulator Assembly\n\nOur Foshan manufacturing facility:\n\nStep 1: Design and Engineering\n- Custom cockpit design\n- Motion platform specification\n\nStep 2: Component Assembly\n- Frame fabrication\n- Actuator installation\n\nStep 3: Integration and Testing\n- Software calibration\n- Quality assurance\n\nStep 4: Delivery\n- Global shipping\n- On-site installation\n\n20+ years of manufacturing excellence. Visit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "industry_news": {
            "title": "Industry Update: The Future of Driving Training",
            "body": "Global Driving Training Market Trends " + str(datetime.now().year) + "\n\nThe driving training industry is rapidly adopting simulation technology:\n\n- Global driving simulator market growing steadily\n- Driving schools adopting simulators for cost reduction\n- Safety-first training becomes industry standard\n\nEasyly Response:\n- Latest 3-6DOF technology\n- Factory-direct global pricing\n- 20+ years of expertise\n\nContact: " + COMPANY["email"] + "\n\n" + " ".join(hashtags[:5])
        },
        "educational": {
            "title": "Why Simulators Improve Training",
            "body": "Why Simulators Are the Future:\n\n1. Safety First\n- Zero risk during initial training\n- Safe practice of emergency scenarios\n\n2. Cost Effective\n- 70-90% lower operational costs\n- No fuel consumption\n\n3. Unlimited Practice\n- 24/7 availability\n- No weather restrictions\n\n4. Standardized Training\n- Consistent training scenarios\n- Measurable progress tracking\n\nData shows: simulators improve efficiency by 40-70%.\n\nVisit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "testimonial": {
            "title": "Customer Testimonial: Easyly Simulators",
            "body": "Real Words from Real Customers:\n\n'We have been using Easyly simulators for " + str(random.randint(6, 24)) + " months:'\n\n- Training costs reduced by " + str(random.randint(60, 90)) + "%\n- Student pass rates improved by " + str(random.randint(20, 40)) + "%\n- Zero safety incidents during simulator training\n- Excellent after-sales support\n\nVisit: " + COMPANY["website_en"] + "\n\n" + " ".join(hashtags[:5])
        },
        "promotional": {
            "title": "Special Offer: Easyly Simulator Packages",
            "body": "Limited-Time " + pi["industry"] + " Package\n\nGet our " + pi["name"] + " (" + pi["model"] + ") with:\n- Free global shipping\n- Professional installation support\n- Comprehensive warranty\n- Free training for staff\n- 24/7 remote technical support\n\nFactory-direct from Foshan Easyly (est. 2004).\nROI typically achieved in 6-12 months.\n\nContact: " + COMPANY["email"] + "\n" + COMPANY["phone"] + "\n\n" + " ".join(hashtags[:5])
        }
    }
    
    t = posts.get(content_type, posts["product_showcase"])
    return {
        "platform": platform,
        "content_type": content_type,
        "title": t["title"],
        "body": t["body"],
        "visual_description": "Product or promotional visual",
        "call_to_action": "Contact: " + COMPANY["email"],
        "hashtags": hashtags[:pc["hashtag_limit"]] if pc["hashtag_limit"] else hashtags,
        "recommended_posting_time": pc["best_posting_times"][0],
        "image_ratio": pc["image_ratio"]
    }

def generate_30_day_calendar():
    calendar = {
        "campaign_name": "Foshan Easyly - 30 Day Social Media Campaign",
        "company": COMPANY["name"],
        "start_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "total_days": 30,
        "posts": []
    }
    
    ct_list = list(CONTENT_TYPES.keys())
    p_list = list(PRODUCTS.keys())
    
    for day in range(1, 31):
        date = (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
        ct = ct_list[day % len(ct_list)]
        prod = p_list[day % len(p_list)]
        
        if day % 5 == 0: platform = "LinkedIn"
        elif day % 7 == 0: platform = "YouTube"
        elif day % 3 == 0: platform = "Instagram"
        elif day % 4 == 0: platform = "TikTok"
        else: platform = "Facebook"
        
        post = generate_post_content(ct, prod, "global", platform)
        post["day"] = day
        post["date"] = date
        post["status"] = "draft"
        calendar["posts"].append(post)
    
    return calendar

def export_calendar(calendar, filename="social_media_calendar.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(calendar, f, indent=2, ensure_ascii=False)
    print("   Exported " + str(len(calendar["posts"])) + " posts to " + filename)

def main():
    print("=" * 80)
    print("Foshan Easyly New Technology Co., Ltd. - Social Media Scheduler")
    print("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 80)
    
    print("\n   Generating 30-day content calendar...")
    calendar = generate_30_day_calendar()
    print("   " + str(len(calendar["posts"])) + " posts scheduled")
    
    print("\n   Platform Breakdown:")
    for platform in PLATFORM_CONFIG:
        count = sum(1 for p in calendar["posts"] if p["platform"] == platform)
        print("   " + platform + ": " + str(count) + " posts")
    
    print("\n   Exporting...")
    export_calendar(calendar)
    
    print("\n   Ready!")

if __name__ == "__main__":
    main()