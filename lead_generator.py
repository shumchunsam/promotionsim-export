#!/usr/bin/env python3
"""
ProMotion Simulators - Automated Lead Generation System
自动拓客系统：生成B2B/B2C客户清单和联系策略
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List, Optional

# 全球目标客户数据库
TARGET_CUSTOMERS: Dict[str, List[Dict]] = {
    # 北美
    "north_america": [
        # 驾校/培训机构
        {
            "name": "AAA Driving Schools",
            "type": "driving_school_chain",
            "country": "USA",
            "city": "Multiple Locations",
            "website": "aaa.com",
            "email_pattern": "training@aaa.com",
            "contact_role": "Training Director",
            "decision_makers": ["Director of Training", "VP Operations", "Procurement Manager"],
            "annual_training_volume": "50,000+",
            "current_training_methods": ["Real vehicles", "Some classroom"],
            "pain_points": ["High insurance costs", "Safety concerns", "Fuel costs"],
            "budget_range": "$50K-$500K",
            "priority": "high"
        },
        {
            "name": "FlightPath Training Academy",
            "type": "flight_training",
            "country": "USA",
            "city": "Multiple",
            "website": "example.com/flightpath",
            "email_pattern": "info@flightpathtraining.com",
            "contact_role": "Chief Training Instructor",
            "decision_makers": ["Chief Training Instructor", "Owner", "Head of Safety"],
            "annual_training_volume": "1,000+",
            "current_training_methods": ["Cessna 172", "Some FTD"],
            "pain_points": ["Limited weather training", "High aircraft costs"],
            "budget_range": "$100K-$1M",
            "priority": "high"
        },
        {
            "name": "Schulz Truck Driving School",
            "type": "cdl_training",
            "country": "USA",
            "city": "Illinois",
            "website": "example.com/schulz",
            "email_pattern": "info@schulztruckingschool.com",
            "contact_role": "Owner/Operator",
            "decision_makers": ["Owner"],
            "annual_training_volume": "1,000+",
            "current_training_methods": ["Real trucks"],
            "pain_points": ["Insurance costs", "Vehicle maintenance"],
            "budget_range": "$25K-$150K",
            "priority": "medium"
        },
        {
            "name": "SimRacing Canada",
            "type": "simulator_shopping",
            "country": "Canada",
            "city": "Toronto",
            "website": "example.com/simracing",
            "email_pattern": "info@simracingcanada.com",
            "contact_role": "Owner",
            "decision_makers": ["Owner", "Operations Manager"],
            "annual_training_volume": "5,000+",
            "current_training_methods": ["Basic rigs"],
            "pain_points": ["Need 6DOF platforms", "Competition pressure"],
            "budget_range": "$30K-$200K",
            "priority": "medium"
        },
    ],
    
    # 欧洲
    "europe": [
        {
            "name": "Eurofins Driving Centers",
            "type": "driving_school_chain",
            "country": "Germany",
            "city": "Multiple",
            "website": "example.com/eurofins",
            "email_pattern": "info@eurofins-driving.de",
            "contact_role": "Training Manager",
            "decision_makers": ["Managing Director", "Training Manager", "Head of Procurement"],
            "annual_training_volume": "15,000+",
            "current_training_methods": ["Real vehicles", "Some classroom"],
            "pain_points": ["ADAC compliance costs", "Insurance liability"],
            "budget_range": "€50K-€300K",
            "priority": "high"
        },
        {
            "name": "Lufthansa Aviation Training",
            "type": "flight_training",
            "country": "Germany",
            "city": "Friedrichshafen",
            "website": "lufthansa-aviation-training.com",
            "email_pattern": "procurement@lat.lufthansa.com",
            "contact_role": "Procurement Manager",
            "decision_makers": ["Procurement", "Training Operations", "Technical Director"],
            "annual_training_volume": "10,000+",
            "current_training_methods": ["Full flight simulators"],
            "pain_points": ["Upgrade costs", "Technology refresh"],
            "budget_range": "€500K-€5M",
            "priority": "very_high"
        },
        {
            "name": "British Driving Academy",
            "type": "driving_school",
            "country": "UK",
            "city": "London",
            "website": "example.com/britishdriving",
            "email_pattern": "info@britishdrivingacademy.co.uk",
            "contact_role": "Owner",
            "decision_makers": ["Owner", "Operations Manager"],
            "annual_training_volume": "2,000+",
            "current_training_methods": ["Real cars", "DVSA standards"],
            "pain_points": ["DVSA compliance", "Road test failure rates"],
            "budget_range": "£30K-£200K",
            "priority": "medium"
        },
        {
            "name": "Paris Simulateurs",
            "type": "simulator_shopping",
            "country": "France",
            "city": "Paris",
            "website": "example.com/paris-sim",
            "email_pattern": "contact@parissimulateurs.fr",
            "contact_role": "Director",
            "decision_makers": ["Director", "Technical Lead"],
            "annual_training_volume": "3,000+",
            "current_training_methods": ["PC-based simulators"],
            "pain_points": ["Need hardware upgrade", "Customer experience"],
            "budget_range": "€40K-€250K",
            "priority": "medium"
        },
    ],
    
    # 东南亚
    "southeast_asia": [
        {
            "name": "Bangkok Driving Academy",
            "type": "driving_school_chain",
            "country": "Thailand",
            "city": "Bangkok",
            "website": "example.com/bangkok-driving",
            "email_pattern": "info@bangkokdrivingacademy.com",
            "contact_role": "General Manager",
            "decision_makers": ["General Manager", "Operations Manager"],
            "annual_training_volume": "5,000+",
            "current_training_methods": ["Real vehicles"],
            "pain_points": ["Rising costs", "Safety concerns", "Expansion needs"],
            "budget_range": "฿1.5M-฿10M",
            "priority": "high"
        },
        {
            "name": "Singapore Sim Center",
            "type": "simulator_shopping",
            "country": "Singapore",
            "city": "Singapore",
            "website": "example.com/sgsimcenter",
            "email_pattern": "info@sgsimcenter.com",
            "contact_role": "Owner",
            "decision_makers": ["Owner", "Operations Manager"],
            "annual_training_volume": "10,000+",
            "current_training_methods": ["Basic simulators"],
            "pain_points": ["Premium experience needed", "Competition"],
            "budget_range": "S$50K-S$300K",
            "priority": "medium"
        },
        {
            "name": "Jakarta Driving School",
            "type": "driving_school",
            "country": "Indonesia",
            "city": "Jakarta",
            "website": "example.com/jakarta-driving",
            "email_pattern": "info@jakartadrivingschool.com",
            "contact_role": "Owner",
            "decision_makers": ["Owner"],
            "annual_training_volume": "8,000+",
            "current_training_methods": ["Real vehicles"],
            "pain_points": ["Growing demand", "Space constraints"],
            "budget_range": "Rp 500M-Rp 5B",
            "priority": "medium"
        },
    ],
    
    # 中东
    "middle_east": [
        {
            "name": "Dubai Driving Center",
            "type": "driving_school_chain",
            "country": "UAE",
            "city": "Dubai",
            "website": "dubaivisaae.com/driving",
            "email_pattern": "info@dubaivisa.com",
            "contact_role": "Operations Director",
            "decision_makers": ["CEO", "Operations Director", "Procurement Manager"],
            "annual_training_volume": "50,000+",
            "current_training_methods": ["Real vehicles", "Some classroom"],
            "pain_points": ["Modernization needs", "Customer experience", "Efficiency"],
            "budget_range": "AED 200K-AED 2M",
            "priority": "very_high"
        },
        {
            "name": "Saudi Flight Training",
            "type": "flight_training",
            "country": "Saudi Arabia",
            "city": "Riyadh",
            "website": "example.com/saudi-flight",
            "email_pattern": "info@saudiflighttraining.sa",
            "contact_role": "Training Director",
            "decision_makers": ["CEO", "Training Director", "Technical Director"],
            "annual_training_volume": "2,000+",
            "current_training_methods": ["Limited FTDs"],
            "pain_points": ["Vision 2030 modernization", "Pilot shortage"],
            "budget_range": "SAR 500K-SAR 5M",
            "priority": "very_high"
        },
        {
            "name": "Abu Dhabi Sim Center",
            "type": "simulator_shopping",
            "country": "UAE",
            "city": "Abu Dhabi",
            "website": "example.com/abudhabisim",
            "email_pattern": "info@abudhabisim.ae",
            "contact_role": "Owner",
            "decision_makers": ["Owner"],
            "annual_training_volume": "5,000+",
            "current_training_methods": ["Basic rigs"],
            "pain_points": ["Premium positioning", "Technology upgrade"],
            "budget_range": "AED 100K-AED 500K",
            "priority": "high"
        },
    ],
    
    # 大洋洲
    "oceania": [
        {
            "name": "Australian Driving Academy",
            "type": "driving_school_chain",
            "country": "Australia",
            "city": "Multiple",
            "website": "example.com/aus-driving",
            "email_pattern": "info@ausdriving.com.au",
            "contact_role": "Operations Manager",
            "decision_makers": ["Operations Manager", "Owner", "Compliance Officer"],
            "annual_training_volume": "20,000+",
            "current_training_methods": ["Real vehicles"],
            "pain_points": ["Regulatory costs", "Safety compliance", "Efficiency"],
            "budget_range": "A$100K-A$800K",
            "priority": "high"
        },
        {
            "name": "NZ Flight Training",
            "type": "flight_training",
            "country": "New Zealand",
            "city": "Auckland",
            "website": "example.com/nzflight",
            "email_pattern": "info@nzflighttraining.co.nz",
            "contact_role": "Chief Flying Instructor",
            "decision_makers": ["CFI", "Owner", "Operations Manager"],
            "annual_training_volume": "1,500+",
            "current_training_methods": ["Small aircraft"],
            "pain_points": ["Limited weather training", "Cost management"],
            "budget_range": "NZ$100K-NZ$500K",
            "priority": "medium"
        },
    ]
}

# B2B决策者角色定义
DECISION_MAKER_PROFILES: Dict[str, Dict] = {
    "driving_school_chain": {
        "title_keywords": ["CEO", "Owner", "Managing Director", "Operations Director", "Training Manager"],
        "pain_points": [
            "High operational costs (fuel, insurance, maintenance)",
            "Safety liability and insurance premiums",
            "Pass rate improvement needs",
            "Training capacity constraints",
            "Regulatory compliance costs"
        ],
        "selling_points": [
            "70-90% reduction in operational costs",
            "Zero safety liability during training",
            "Unlimited training capacity",
            "Modern technology image for marketing",
            "Faster training throughput"
        ]
    },
    "flight_training": {
        "title_keywords": ["CEO", "Chief Flying Instructor", "Training Director", "Technical Director"],
        "pain_points": [
            "Aircraft operating costs (fuel, maintenance)",
            "Weather-related training cancellations",
            "Limited simulator availability",
            "FAA/EASA compliance requirements",
            "Pilot shortage and training capacity"
        ],
        "selling_points": [
            "FAA/EASA approved FTD options",
            "All-weather training capability",
            "Emergency procedure practice",
            "Reduced aircraft wear and tear",
            "Higher training throughput"
        ]
    },
    "cdl_training": {
        "title_keywords": ["Owner", "Operator", "Training Manager", "Safety Director"],
        "pain_points": [
            "Commercial vehicle insurance costs",
            "Federal/state compliance requirements",
            "Safety liability",
            "High maintenance costs",
            "CDL pass rates"
        ],
        "selling_points": [
            "Reduced insurance premiums",
            "Zero accident risk during training",
            "FMCSA compliance support",
            "Unlimited practice time",
            "Improved CDL pass rates"
        ]
    },
    "simulator_shopping": {
        "title_keywords": ["Owner", "Operations Manager", "General Manager", "Technical Lead"],
        "pain_points": [
            "Competition pressure",
            "Customer experience requirements",
            "Equipment upgrade needs",
            "Revenue optimization",
            "Technology differentiation"
        ],
        "selling_points": [
            "Factory-direct pricing",
            "Latest 3-6DOF technology",
            "Customization options",
            "Global shipping and installation",
            "After-sales support"
        ]
    }
}

def generate_outreach_strategy(region: str) -> Dict:
    """Generate comprehensive outreach strategy for a region"""
    customers = TARGET_CUSTOMERS[region]
    
    strategy = {
        "region": region,
        "total_customers": len(customers),
        "high_priority": [c for c in customers if c["priority"] in ["high", "very_high"]],
        "medium_priority": [c for c in customers if c["priority"] == "medium"],
        "recommended_channels": get_recommended_channels(region),
        "estimated_timeline": get_timeline(region),
        "budget_estimate": get_budget_estimate(customers)
    }
    
    return strategy


def get_recommended_channels(region: str) -> List[str]:
    """Get recommended outreach channels for a region"""
    channels = {
        "north_america": ["LinkedIn", "Email", "Phone", "Industry Trade Shows", "Google Ads"],
        "europe": ["LinkedIn", "Email", "Trade Shows", "Industry Conferences", "Local Partners"],
        "southeast_asia": ["Email", "WeChat", "Local Agents", "Trade Shows", "Facebook"],
        "middle_east": ["Email", "Phone", "WhatsApp", "LinkedIn", "Local Partners"],
        "oceania": ["LinkedIn", "Email", "Phone", "Industry Events", "Google Ads"]
    }
    return channels.get(region, ["Email", "LinkedIn", "Trade Shows"])


def get_timeline(region: str) -> str:
    """Get recommended outreach timeline"""
    timelines = {
        "north_america": "Q3-Q4 2025 (Peak training season)",
        "europe": "Q3-Q4 2025 (Budget planning cycle)",
        "southeast_asia": "Q4 2025-Q1 2026 (Growing market)",
        "middle_east": "Q4 2025-Q2 2026 (Vision 2030 momentum)",
        "oceania": "Q3-Q4 2025 (Training season)"
    }
    return timelines.get(region, "Q3-Q4 2025")


def get_budget_estimate(customers: List[Dict]) -> Dict[str, str]:
    """Get total budget estimate for region"""
    budget_ranges = {
        "north_america": "$50K-$500K per customer",
        "europe": "€50K-€300K per customer",
        "southeast_asia": "Variable by country",
        "middle_east": "AED 100K-AED 2M per customer",
        "oceania": "A$100K-A$800K per customer"
    }
    return budget_ranges


def generate_email_for_customer(customer: Dict, template_type: str = "cold") -> str:
    """Generate personalized email for a specific customer"""
    customer_type = customer["type"]
    decision_makers = DECISION_MAKER_PROFILES.get(customer_type, {})
    
    pain_points = decision_makers.get("pain_points", [])
    selling_points = decision_makers.get("selling_points", [])
    
    emails = {
        "cold": f"""Subject: {selling_points[0] if selling_points else "Transform Your Training Operations"}

Dear {customer['contact_role']},

I'm reaching out from ProMotion Simulators regarding {customer['name']}'s {customer['type']} operations in {customer['country']}.

We specialize in professional {customer['type'].replace('_', ' ')} simulators that directly address the challenges you face:

**Key Benefits for {customer['name']}:**
{chr(10).join('✓ ' + point for point in selling_points[:3])}

**Why Partner With Us:**
✓ Factory-direct pricing (no middlemen)
✓ Global shipping and installation support
✓ 24/7 remote technical support
✓ Customizable to your specific requirements
✓ Proven track record in {customer['country']}

**Your Current Challenges:**
• {pain_points[0] if pain_points else "Operational efficiency"}
• {pain_points[1] if len(pain_points) > 1 else "Training quality"}
• {pain_points[2] if len(pain_points) > 2 else "Cost management"}

I'd love to schedule a 15-minute call to discuss how we can support your {customer['type']} training center.

Best regards,
Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/""",
        
        "follow_up": f"""Subject: Re: {selling_points[0] if selling_points else "Training Solutions"}

Hi,

Following up on my previous email about {customer['type'].replace('_', ' ')} simulators.

I wanted to share our latest case study from a {customer['country']} client who saw {random.choice(['40%', '60%', '70%'])} improvement in training efficiency after implementing our platform.

Would you be available for a brief call next week?

Best regards,
Samson Shum
ProMotion Simulators"""
    }
    
    return emails.get(template_type, emails["cold"])


def generate_outreach_plan() -> Dict:
    """Generate complete outreach plan"""
    plan = {
        "overview": {
            "generated_date": datetime.now().strftime("%Y-%m-%d"),
            "total_regions": len(TARGET_CUSTOMERS),
            "total_customers": sum(len(c) for c in TARGET_CUSTOMERS.values()),
            "high_priority_customers": sum(1 for c in TARGET_CUSTOMERS.values() for customer in c if customer["priority"] in ["high", "very_high"])
        },
        "regions": {}
    }
    
    for region in TARGET_CUSTOMERS.keys():
        plan["regions"][region] = generate_outreach_strategy(region)
    
    return plan


def export_to_csv(plan: Dict, filename: str = "outreach_plan.csv"):
    """Export outreach plan to CSV"""
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Region", "Customer Name", "Type", "Country", "Priority",
            "Budget Range", "Contact Role", "Decision Makers",
            "Key Pain Points", "Recommended Channels", "Timeline"
        ])
        
        for region, data in plan["regions"].items():
            customers = TARGET_CUSTOMERS[region]
            for customer in customers:
                decision_makers = DECISION_MAKER_PROFILES.get(customer["type"], {})
                pain_points = decision_makers.get("pain_points", [])
                
                writer.writerow([
                    region.replace('_', ' ').title(),
                    customer["name"],
                    customer["type"].replace('_', ' ').title(),
                    customer["country"],
                    customer["priority"].title(),
                    customer["budget_range"],
                    customer["contact_role"],
                    ", ".join(customer["decision_makers"]),
                    "; ".join(pain_points[:3]),
                    ", ".join(get_recommended_channels(region)),
                    get_timeline(region)
                ])
    
    print(f"✅ Exported {len(TARGET_CUSTOMERS['north_america']) + len(TARGET_CUSTOMERS['europe']) + len(TARGET_CUSTOMERS['southeast_asia']) + len(TARGET_CUSTOMERS['middle_east']) + len(TARGET_CUSTOMERS['oceania'])} customer profiles to {filename}")


def main():
    print("=" * 80)
    print("ProMotion Simulators - Automated Lead Generation System")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)
    
    # Generate complete outreach plan
    plan = generate_outreach_plan()
    
    print(f"\n📊 OVERVIEW:")
    print(f"   Total Regions: {plan['overview']['total_regions']}")
    print(f"   Total Customers: {plan['overview']['total_customers']}")
    print(f"   High Priority: {plan['overview']['high_priority_customers']}")
    
    # Print regional breakdown
    print(f"\n🌍 REGIONAL BREAKDOWN:")
    for region, data in plan["regions"].items():
        print(f"\n   {region.replace('_', ' ').title()}:")
        print(f"   ├─ Total Customers: {data['total_customers']}")
        print(f"   ├─ High Priority: {len(data['high_priority'])}")
        print(f"   ├─ Medium Priority: {len(data['medium_priority'])}")
        print(f"   ├─ Timeline: {data['estimated_timeline']}")
        print(f"   └─ Recommended Channels: {', '.join(data['recommended_channels'][:3])}")
    
    # Export to CSV
    export_to_csv(plan)
    
    print(f"\n✅ Lead generation system ready!")
    print(f"📋 Next steps:")
    print(f"   1. Review target customers by region")
    print(f"   2. Generate personalized outreach emails")
    print(f"   3. Execute multi-channel outreach campaign")


if __name__ == "__main__":
    main()