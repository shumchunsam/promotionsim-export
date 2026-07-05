#!/usr/bin/env python3
"""
ProMotion Simulators - Automated Social Media Scheduler
自动生成30天社媒内容日历，支持多平台和多语言
"""

import json
import os
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# 产品定义
PRODUCTS = {
    "automotive": {"name": "Driving Simulator", "emoji": "🚗", "industry": "Automotive"},
    "flight": {"name": "Flight Simulator", "emoji": "✈️", "industry": "Aviation"},
    "heavy_vehicle": {"name": "Truck/Bus Simulator", "emoji": "🚌", "industry": "Commercial"},
    "motion_platform": {"name": "Motion Platform", "emoji": "🏭", "industry": "Industrial"}
}

# 内容类型
CONTENT_TYPES = {
    "product_showcase": {
        "title": "Product Showcase",
        "description": "展示产品细节、技术规格",
        "platforms": ["LinkedIn", "Instagram", "YouTube"]
    },
    "customer_story": {
        "title": "Customer Success Story",
        "description": "客户案例、使用场景",
        "platforms": ["LinkedIn", "Facebook"]
    },
    "technical_insight": {
        "title": "Technical Insight",
        "description": "技术原理、行业分析",
        "platforms": ["LinkedIn", "YouTube"]
    },
    "behind_the_scenes": {
        "title": "Behind the Scenes",
        "description": "工厂实拍、组装过程",
        "platforms": ["Instagram", "TikTok", "YouTube Shorts"]
    },
    "industry_news": {
        "title": "Industry News",
        "description": "行业动态、市场趋势",
        "platforms": ["LinkedIn", "Twitter"]
    },
    "educational": {
        "title": "Educational Content",
        "description": "培训知识、安全科普",
        "platforms": ["Facebook", "YouTube", "LinkedIn"]
    },
    "testimonial": {
        "title": "Testimonial",
        "description": "客户评价、推荐",
        "platforms": ["LinkedIn", "Facebook", "YouTube"]
    },
    "promotional": {
        "title": "Promotional",
        "description": "促销活动、折扣信息",
        "platforms": ["Instagram", "Facebook", "LinkedIn"]
    }
}

# 平台特定配置
PLATFORM_CONFIG = {
    "LinkedIn": {
        "max_characters": 3000,
        "best_posting_times": ["Tuesday 10:00 AM", "Wednesday 9:00 AM", "Thursday 11:00 AM"],
        "hashtag_limit": 5,
        "tone": "Professional, B2B-focused",
        "image_ratio": "1200x627px",
        "video_max_length": "10 minutes"
    },
    "Instagram": {
        "max_characters": 2200,
        "best_posting_times": ["Monday-Friday 11:00 AM-1:00 PM", "Saturday 10:00 AM-11:00 AM"],
        "hashtag_limit": 30,
        "tone": "Visual, engaging, slightly informal",
        "image_ratio": "1:1 or 4:5",
        "video_max_length": "60 seconds (Reels)"
    },
    "YouTube": {
        "max_characters": 5000,
        "best_posting_times": ["Monday-Wednesday 2:00-4:00 PM", "Friday 1:00-3:00 PM"],
        "hashtag_limit": 15,
        "tone": "Informative, high-quality production",
        "image_ratio": "16:9 thumbnails",
        "video_max_length": "Unlimited"
    },
    "Facebook": {
        "max_characters": 63206,
        "best_posting_times": ["Monday-Friday 1:00-3:00 PM", "Saturday 9:00-11:00 AM"],
        "hashtag_limit": None,
        "tone": "Community-focused, family-friendly",
        "image_ratio": "1200x630px",
        "video_max_length": "240 minutes"
    },
    "TikTok": {
        "max_characters": 2200,
        "best_posting_times": ["Monday-Friday 6:00-10:00 AM", "12:00-1:00 PM", "7:00-11:00 PM"],
        "hashtag_limit": None,
        "tone": "Casual, trending, engaging",
        "image_ratio": "9:16 vertical",
        "video_max_length": "10 minutes (recommended 15-60s)"
    }
}

def generate_hashtags(content_type: str, product: str, region: str = "global") -> List[str]:
    """Generate platform-specific hashtags"""
    base_hashtags = {
        "driving_simulator": ["#drivingsimulator", "#drivingtraining", "#drivertraining", "#simracing"],
        "flight_simulator": ["#flightsimulator", "#pilottraining", "#aviation", "#flightsimulation"],
        "heavy_vehicle": ["#truckdriver", "#commercialdriving", "#CDLtraining", "#busdriving"],
        "motion_platform": ["#motionplatform", "#6DOF", "#3DOF", "#simulatorplatform", "#motionstage"]
    }
    
    regional_hashtags = {
        "global": [],
        "north_america": ["#USAdriving", "#CanadaTraining", "#NorthAmericaSim"],
        "europe": ["#EuroDriving", "#UKTraining", "#GermanDriving", "#FSDriving"],
        "southeast_asia": ["#ThaiDriving", "#SGTraining", "#MalaysiaSim"],
        "middle_east": ["#UAEDriving", "#SaudiTraining", "#QatarSim"],
        "oceania": ["#AusDriving", "#NZTraining"]
    }
    
    trending_hashtags = [
        f"{datetime.now().year}", "#VRsimulator", "#immersivelearning",
        "#safetytraining", "#protrainingsim"
    ]
    
    hashtags = base_hashtags.get(product, [])
    hashtags.extend(regional_hashtags.get(region, []))
    hashtags.extend(trending_hashtags)
    
    return list(set(hashtags))  # Remove duplicates


def generate_post_content(content_type: str, product: str, region: str, platform: str) -> Dict:
    """Generate post content for specific content type"""
    product_info = PRODUCTS[product]
    platform_config = PLATFORM_CONFIG[platform]
    content_config = CONTENT_TYPES[content_type]
    
    hashtags = generate_hashtags(content_type, product, region)
    
    content_templates = {
        "product_showcase": {
            "title": f"🎯 {product_info['name']} - Precision Engineering at Its Best",
            "body": f"""{product_info['emoji']} Introducing our latest {product_info['name']} from ProMotion Simulators.

Engineered for {product_info['industry']} professionals, our {product_info['name']} delivers:
✓ Industry-leading motion fidelity
✓ Custom cockpit configurations
✓ Global shipping & installation
✓ 24/7 remote technical support

Perfect for:
• Driving schools & training centers
• Aviation academies
• Simulator shops & entertainment venues
• Government & military training

Factory-direct pricing with worldwide delivery.

#drivingsimulator #flightsimulator #motionplatform #simulation #protrainingsim""",
            "visual_description": "Product showcase video showing the simulator in operation with dynamic motion",
            "call_to_action": "🔗 Visit our website for full specifications: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "customer_story": {
            "title": "🌟 Customer Success: [Client Name] Transforms Training with Simulators",
            "body": f"""📈 Real Results from Real Customers

[Client Name] implemented our {product_info['name']} and saw:
• 70% reduction in training costs
• 40% improvement in training efficiency
• Zero safety incidents during training
• 25% increase in student throughput

"This simulator has revolutionized how we train. The investment paid for itself in just 8 months." - [Training Director]

Ready to transform your training program?

#customersuccess #drivingsimulator #flightsimulator #training #innovation""",
            "visual_description": "Before/after comparison showing training center transformation",
            "call_to_action": "📧 Contact us for case studies: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "technical_insight": {
            "title": "🔬 Technical Deep Dive: How 6DOF Motion Platforms Work",
            "body": f"""⚙️ Understanding {product_info['name']} Technology

The secret behind realistic simulation lies in motion platforms:

📐 Degrees of Freedom (DOF):
• 3DOF: Pitch, Roll, Yaw (basic motion)
• 4DOF: Adds Heave (vertical)
• 6DOF: Full motion - Pitch, Roll, Yaw, Heave, Surge, Sway

🔧 Key Components:
• Linear actuators for precise movement
• Real-time control algorithms
• Professional-grade sensors
• Custom-tuned motion profiles

Our 6DOF platforms replicate:
✓ Vehicle dynamics
✓ Flight movements
✓ Emergency scenarios
✓ Weather effects

🔍 Want to learn more about simulation technology?

#motionplatform #6DOF #simulation #engineering #technology""",
            "visual_description": "Technical diagram or animation showing 6DOF movement axes",
            "call_to_action": "📚 Read our technical whitepaper: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "behind_the_scenes": {
            "title": "🏭 Behind the Scenes: Building a {product_info['name']}",
            "body": f"""🔧 Inside Our Factory: {product_info['name']} Assembly Process

Take a peek inside our manufacturing facility as we build a custom {product_info['name']}:

📋 Step 1: Design & Engineering
• 3D modeling & simulation
• Custom cockpit design
• Motion platform specification

📋 Step 2: Component Assembly
• Frame fabrication
• Actuator installation
• Electrical wiring

📋 Step 3: Integration & Testing
• Software installation
• Motion calibration
• Quality assurance testing

📋 Step 4: Delivery
• Professional packaging
• Global shipping
• On-site installation

Factory-direct means direct quality control at every step.

#behindthescenes #factory #manufacturing #quality #engineering""",
            "visual_description": "Time-lapse video of simulator assembly process",
            "call_to_action": "🏭 Visit our factory tour: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "industry_news": {
            "title": "📰 Industry Update: The Future of Simulation Training",
            "body": f"""🌍 Global Simulation Training Market Trends {datetime.now().year}

The {product_info['industry']} simulation industry is growing rapidly:

📊 Market Insights:
• Global driving simulator market: $2.1B (2025)
• Flight training simulators: $1.8B (2025)
• Expected CAGR: 8.5% through 2030

🔮 Key Trends:
• Increased adoption of VR/AR technology
• Growing demand for cost-effective training
• Regulatory compliance requirements
• Skill shortage in {product_info['industry']} sectors

🌐 Our Response:
• Latest 6DOF technology
• Custom configurations for all markets
• Global shipping & support
• Competitive factory-direct pricing

Stay ahead of the curve with ProMotion Simulators.

#industrynews #simulation #training #innovation #futureoftraining""",
            "visual_description": "Infographic showing market growth and trends",
            "call_to_action": "📊 Download our market report: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "educational": {
            "title": "🎓 Educational Series: Understanding Simulator Training Benefits",
            "body": f"""📚 Why Simulators are the Future of Training

🤔 How do simulators improve training outcomes?

1️⃣ Safety First
• Zero risk during initial training
• Safe practice of emergency scenarios
• Reduced insurance liability

2️⃣ Cost Effective
• 70-90% lower operational costs
• No fuel consumption
• Minimal maintenance

3️⃣ Unlimited Practice
• 24/7 availability
• No weather restrictions
• Faster skill acquisition

4️⃣ Standardized Training
• Consistent training scenarios
• Measurable progress tracking
• Repeatable emergency situations

💡 The data is clear: simulators improve training efficiency by 40-70%.

What training challenges are you facing?

#educational #training #safety #costeffective #innovation""",
            "visual_description": "Infographic comparing simulator vs traditional training costs",
            "call_to_action": "💡 Learn more about training benefits: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "testimonial": {
            "title": "⭐ Customer Testimonial: [Client Name] Shares Their Experience",
            "body": f"""💬 Real Words from Real Customers

"[Client Name] - {product_info['industry']} Training Center"

"We've been using ProMotion's {product_info['name']} for [X] months and the results speak for themselves:

✓ Training costs reduced by {random.randint(60, 90)}%
✓ Student pass rates improved by {random.randint(20, 40)}%
✓ Zero safety incidents during simulator training
✓ Excellent after-sales support
✓ Fast global delivery

The investment paid for itself within [X] months. Highly recommended for any training center looking to modernize.

Thank you, ProMotion Simulators! 🙏

#testimonial #customersuccess #drivingsimulator #flightsimulator #quality""",
            "visual_description": "Customer testimonial video or quote graphic",
            "call_to_action": "📞 Get your quote: https://shumchunsam.github.io/promotionsim-export/"
        },
        
        "promotional": {
            "title": "🎉 Special Offer: {product_info['name']} Packages",
            "body": f"""🔥 Limited-Time {product_info['industry']} Training Package

Get our {product_info['name']} with:
✅ Free global shipping
✅ Professional installation support
✅ 2-year comprehensive warranty
✅ Free training for your staff
✅ 24/7 remote technical support

Perfect for:
• New training centers
• Upgrading existing facilities
• Expansion projects

📈 ROI typically achieved in 6-12 months

📞 Contact us for a customized quote:
https://shumchunsam.github.io/promotionsim-export/

Don't miss out on this opportunity to modernize your training program!

#promotional #specialoffer #drivingsimulator #flightsimulator #simulator""",
            "visual_description": "Promotional graphic with offer details",
            "call_to_action": "🎁 Claim your offer now: https://shumchunsam.github.io/promotionsim-export/"
        }
    }
    
    template = content_templates.get(content_type, content_templates["product_showcase"])
    
    return {
        "platform": platform,
        "content_type": content_type,
        "title": template["title"],
        "body": template["body"],
        "visual_description": template["visual_description"],
        "call_to_action": template["call_to_action"],
        "hashtags": hashtags[:platform_config["hashtag_limit"]] if platform_config["hashtag_limit"] else hashtags,
        "recommended_posting_time": platform_config["best_posting_times"][0],
        "image_ratio": platform_config["image_ratio"]
    }


def generate_30_day_calendar() -> Dict:
    """Generate 30-day social media content calendar"""
    calendar = {
        "campaign_name": "ProMotion Simulators - 30 Day Social Media Campaign",
        "start_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        "total_days": 30,
        "content_types": list(CONTENT_TYPES.keys()),
        "products": list(PRODUCTS.keys()),
        "platforms": list(PLATFORM_CONFIG.keys()),
        "posts": []
    }
    
    content_types_list = list(CONTENT_TYPES.keys())
    products_list = list(PRODUCTS.keys())
    
    for day in range(1, 31):
        date = (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
        day_of_week = datetime.now() + timedelta(days=day)
        
        # Select content type (cycle through)
        content_type = content_types_list[day % len(content_types_list)]
        
        # Select product (rotate)
        product = products_list[day % len(products_list)]
        
        # Select platform
        if day % 5 == 0:
            platform = "LinkedIn"  # B2B focus every 5th day
        elif day % 7 == 0:
            platform = "YouTube"  # Video content weekly
        elif day % 3 == 0:
            platform = "Instagram"
        elif day % 4 == 0:
            platform = "TikTok"
        else:
            platform = "Facebook"
        
        post = generate_post_content(content_type, product, "global", platform)
        post["day"] = day
        post["date"] = date
        post["status"] = "draft"
        
        calendar["posts"].append(post)
    
    return calendar


def export_calendar(calendar: Dict, filename: str = "social_media_calendar.json"):
    """Export calendar to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(calendar, f, indent=2, ensure_ascii=False)
    print(f"✅ Exported {len(calendar['posts'])} posts to {filename}")


def generate_platform_specific_content(calendar: Dict) -> Dict:
    """Generate platform-specific content variations"""
    platform_content = {platform: [] for platform in PLATFORM_CONFIG.keys()}
    
    for post in calendar["posts"]:
        platform = post["platform"]
        platform_content[platform].append(post)
    
    return platform_content


def main():
    print("=" * 80)
    print("ProMotion Simulators - Social Media Scheduler")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)
    
    # Generate 30-day calendar
    print("\n📅 Generating 30-day content calendar...")
    calendar = generate_30_day_calendar()
    print(f"   ✓ {len(calendar['posts'])} posts scheduled")
    print(f"   ✓ Calendar: {calendar['start_date']} to {(datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')}")
    
    # Generate platform-specific breakdown
    print("\n📱 Platform Breakdown:")
    platform_content = generate_platform_specific_content(calendar)
    for platform, posts in platform_content.items():
        print(f"   {platform}: {len(posts)} posts")
    
    # Export to JSON
    print("\n📁 Exporting calendar...")
    export_calendar(calendar)
    
    # Show sample posts
    print(f"\n📝 Sample Posts:")
    for i, post in enumerate(calendar["posts"][:5]):
        print(f"\n   Day {post['day']} ({post['date']}):")
        print(f"   Platform: {post['platform']}")
        print(f"   Type: {post['content_type']}")
        print(f"   Title: {post['title'][:60]}...")
        print(f"   Hashtags: {len(post['hashtags'])} hashtags")
    
    print(f"\n✅ Social media scheduler ready!")
    print(f"📋 Next steps:")
    print(f"   1. Review and customize posts by platform")
    print(f"   2. Create visual content for each post")
    print(f"   3. Schedule posting times")


if __name__ == "__main__":
    main()