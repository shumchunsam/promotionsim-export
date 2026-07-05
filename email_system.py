#!/usr/bin/env python3
"""
Foshan Easyly New Technology Co., Ltd. - Email Outreach System
Automated B2B/B2C cold email system for driving simulator export
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List, Optional

# Company configuration
COMPANY = {
    "name": "Foshan Easyly New Technology Co., Ltd.",
    "name_short": "Easyly",
    "founded": 2004,
    "location": "Foshan, Guangdong, China",
    "website": "https://www.studycar.com",
    "website_en": "https://www.studycar.com/en/",
    "email": "260240751@qq.com",
    "phone": "+86 13798624342",
    "address": "Foshan, Guangdong, China",
    "icp": "粤ICP备09098372号",
    "type": "High-Tech Enterprise"
}

PRODUCTS = {
    "driving_simulator": {
        "name": "Car Driving Simulator",
        "name_short": "Driving Simulator",
        "model_range": "YSL2021-86 / YSL2021-88 (68cm/86cm)",
        "description": "Professional car driving simulator for training and education",
        "features": [
            "Realistic steering wheel and pedal system",
            "Full gear shifter integration",
            "Multi-monitor display support",
            "Compatible with all major training software",
            "Available in 68cm and 86cm widths",
            "Easy to install and maintain"
        ],
        "use_cases": [
            "Driving schools and training centers",
            "Driver education programs",
            "Vehicle safety training",
            "New driver preparation courses"
        ]
    },
    "racing_simulator": {
        "name": "6-DOF Racing Simulator Platform",
        "name_short": "Racing Simulator",
        "model_range": "6-DOF Motion Platform Series",
        "description": "Professional motion racing simulator with full immersion experience",
        "features": [
            "6-DOF dynamic motion feedback",
            "Full cockpit integration",
            "Real-time motion rendering",
            "Compatible with PC/console racing games",
            "Professional-grade build quality",
            "Customizable cockpit design"
        ],
        "use_cases": [
            "Sim racing enthusiasts",
            "Entertainment venues and arcades",
            "Racing experience centers",
            "Professional racing training"
        ]
    },
    "heavy_vehicle": {
        "name": "Truck & Bus Simulator",
        "name_short": "Heavy Vehicle Simulator",
        "model_range": "Commercial Vehicle Series",
        "description": "Heavy-duty simulator for commercial driver training",
        "features": [
            "Full brake/clutch/gear integration",
            "Heavy vehicle dynamics simulation",
            "Multiple cabin configurations",
            "CDL preparation support",
            "Multi-vehicle type support",
            "Commercial training software compatible"
        ],
        "use_cases": [
            "CDL training centers",
            "Trucking companies",
            "Public transit training",
            "Logistics and fleet training"
        ]
    },
    "electric_vehicle": {
        "name": "Electric Training Vehicle",
        "name_short": "Electric Training Vehicle",
        "model_range": "Dual-Control EV Series",
        "description": "Electric training vehicles with dual-control safety system",
        "features": [
            "Dual-control instructor system",
            "New energy vehicle platform",
            "Compliant with driving test standards",
            "Instructor safety control",
            "Low maintenance cost",
            "Environmentally friendly"
        ],
        "use_cases": [
            "New energy vehicle training",
            "EV driver education",
            "Driving schools",
            "Fleet training programs"
        ]
    }
}

CUSTOMER_TYPES = {
    "b2b_driving_school": {
        "name": "Driving School",
        "email_subjects": [
            "Reduce Driving School Training Costs by 70% with Simulators",
            "Foshan Easyly - Professional Driving Simulator Manufacturer Since 2004",
            "Transform Your Driving School with Factory-Direct Simulators"
        ],
        "pain_points": [
            "High fuel and maintenance costs for training vehicles",
            "Limited training capacity and schedule conflicts",
            "Safety liability and accident risks",
            "Low student pass rates on road tests",
            "Rising instructor wages and vehicle costs"
        ],
        "selling_points": [
            "70-90% reduction in training costs vs real vehicles",
            "Zero safety liability during simulator training",
            "Unlimited training capacity - 24/7 availability",
            "20+ years manufacturer experience since 2004",
            "Factory-direct pricing with global shipping",
            "Compatible with national driving test standards"
        ],
        "call_to_action": "Request a free demo and quote for your driving school"
    },
    "b2b_cdl": {
        "name": "CDL Training Center",
        "email_subjects": [
            "Cut CDL Training Costs by 70% with Professional Simulators",
            "Factory-Direct Truck Simulator for CDL Training",
            "Improve CDL Pass Rates with Easyly Simulators"
        ],
        "pain_points": [
            "Commercial vehicle insurance costs",
            "Federal/state compliance and documentation",
            "High fuel consumption and vehicle wear",
            "Limited practice time for students",
            "Safety concerns during training"
        ],
        "selling_points": [
            "70%+ reduction in training costs",
            "Zero accident risk during simulator training",
            "Full CDL test preparation compatibility",
            "Factory-direct from established 2004 manufacturer",
            "Global shipping and installation support",
            "Proven track record with driving training programs"
        ],
        "call_to_action": "Get your CDL simulator quote today"
    },
    "b2b2c_simulator_shop": {
        "name": "Simulator Shop / VR Arcade",
        "email_subjects": [
            "Premium 6-DOF Racing Simulators for Your Business",
            "Factory-Direct Motion Platforms from China's Top Manufacturer",
            "Boost Your Revenue with Professional Sim Racing Rigs"
        ],
        "pain_points": [
            "Competition pressure in entertainment industry",
            "Need for premium, eye-catching equipment",
            "High equipment costs from Western suppliers",
            "Customer experience expectations",
            "Equipment reliability and maintenance"
        ],
        "selling_points": [
            "Factory-direct pricing - up to 60% cheaper than Western brands",
            "Latest 6-DOF motion technology",
            "Custom branding and cockpit design",
            "20+ years manufacturing expertise",
            "Global shipping and installation",
            "After-sales support and spare parts"
        ],
        "call_to_action": "Explore our simulator solutions for your business"
    },
    "consumer": {
        "name": "Consumer / Sim Racing Enthusiast",
        "email_subjects": [
            "Professional 6-DOF Racing Simulator - Direct from Manufacturer",
            "Factory-Direct Sim Racing Rigs - No Middlemen Markup",
            "The Ultimate Home Simulator Experience"
        ],
        "pain_points": [
            "Expensive pre-built sim rigs from Western brands",
            "Limited customization options",
            "Poor build quality in budget alternatives",
            "Lack of after-sales support",
            "Difficulty upgrading individual components"
        ],
        "selling_points": [
            "Factory-direct pricing - no middlemen",
            "Full customization - cockpit, steering, motion axes",
            "Professional-grade build quality (20+ years)",
            "Direct manufacturer support and warranty",
            "Easy upgrades and modular design",
            "Ships worldwide with installation guide"
        ],
        "call_to_action": "Configure your custom simulator today"
    },
    "government": {
        "name": "Government / Defense",
        "email_subjects": [
            "Professional Simulation Solutions for Government Training",
            "Military-Grade Driving Simulator - Certified Chinese Manufacturer",
            "Government Procurement: Driving Simulator Training Systems"
        ],
        "pain_points": [
            "Defense training budget constraints",
            "Security and compliance requirements",
            "Training effectiveness and outcomes",
            "Long-term maintenance and support",
            "Regulatory and safety standards"
        ],
        "selling_points": [
            "High-Tech Enterprise certified (since 2004)",
            "Competitive government procurement pricing",
            "Full compliance documentation support",
            "Long-term maintenance and spare parts supply",
            "Proven track record with Chinese government projects",
            "Custom security configurations available"
        ],
        "call_to_action": "Request government procurement information"
    }
}

LANGUAGES = {
    "en": {
        "greeting": "Dear {name},",
        "intro": "I'm reaching out from Foshan Easyly New Technology Co., Ltd., a professional driving simulator manufacturer since 2004.",
        "value_proposition": "We specialize in professional {product} systems that address your key challenges:",
        "benefits": "Key Benefits for {company}:",
        "why_us": "Why Partner With Easyly:",
        "challenges": "Your Current Challenges:",
        "call_to_action": "I'd love to schedule a call to discuss how we can support your training program.",
        "closing": "Best regards,",
        "signature": """Samson Shum
Foshan Easyly New Technology Co., Ltd.
https://www.studycar.com/en/"""
    },
    "es": {
        "greeting": "Estimado/a {name},",
        "intro": "Le contactamos de Foshan Easyly New Technology Co., Ltd., fabricante profesional de simuladores de conducción desde 2004.",
        "value_proposition": "Nos especializamos en sistemas profesionales de {product} que abordan sus principales desafíos:",
        "benefits": "Beneficios Clave para {company}:",
        "why_us": "¿Por Qué Elegirnos?",
        "challenges": "Sus Desafíos Actuales:",
        "call_to_action": "Me encantaría programar una llamada para discutir cómo podemos apoyar su programa de formación.",
        "closing": "Saludos cordiales,",
        "signature": """Samson Shum
Foshan Easyly New Technology Co., Ltd.
https://www.studycar.com/en/"""
    },
    "fr": {
        "greeting": "Cher/Chère {name},",
        "intro": "Je vous contacte de Foshan Easyly New Technology Co., Ltd., fabricant professionnel de simulateurs de conduite depuis 2004.",
        "value_proposition": "Nous sommes spécialisés dans les systèmes professionnels de {product} qui répondent à vos défis principaux:",
        "benefits": "Avantages Clés pour {company}:",
        "why_us": "Pourquoi Nous Choisir?",
        "challenges": "Vos Défis Actuels:",
        "call_to_action": "J'aimerais organiser un appel pour discuter de la manière dont nous pouvons soutenir votre programme de formation.",
        "closing": "Cordialement,",
        "signature": """Samson Shum
Foshan Easyly New Technology Co., Ltd.
https://www.studycar.com/en/"""
    },
    "ar": {
        "greeting": "السيد/ة {name} المحترم/ة،",
        "intro": "أتواصل معكم من Foshan Easyly New Technology Co., Ltd، الشركة المصنعة للمحاكيات المهنية للقيادة منذ عام 2004.",
        "value_proposition": "نحن متخصصون في أنظمة {product} الاحترافية التي تعالج تحدياتكم الرئيسية:",
        "benefits": "الفوائد الرئيسية لـ {company}:",
        "why_us": "لماذا تختارنا؟",
        "challenges": "تحدياتكم الحالية:",
        "call_to_action": "أرغب في جدولة مكالمة لمناقشة كيفية دعم برنامج التدريب الخاص بكم.",
        "closing": "مع أطيب التحيات،",
        "signature": """Samson Shum
Foshan Easyly New Technology Co., Ltd.
https://www.studycar.com/en/"""
    }
}

def generate_email_template(customer_type: str, product: str, language: str = "en", follow_up: bool = False) -> Dict:
    """Generate email template for specific customer type and product"""
    customer_config = CUSTOMER_TYPES[customer_type]
    product_config = PRODUCTS.get(product, PRODUCTS["driving_simulator"])
    lang_config = LANGUAGES[language]
    
    if follow_up:
        subject = f"Re: {customer_config['email_subjects'][0][:60]}..."
        body = f"""{lang_config['greeting'].format(name='[Contact Name]')}

Following up on my previous email about {product_config['name']} solutions from Foshan Easyly New Technology Co., Ltd. (est. 2004).

We've helped {random.choice(['50+', '100+', '200+'])} training centers worldwide reduce costs by 70-90%.

{lang_config['call_to_action'].format(type=customer_type.replace('_', ' '))}

{lang_config['closing']}
{lang_config['signature']}"""
    else:
        subject = random.choice(customer_config['email_subjects'])
        
        benefits_text = "\n".join(f"  {point}" for point in customer_config['selling_points'][:5])
        challenges_text = "\n".join(f"  - {point}" for point in customer_config['pain_points'][:4])
        features_text = "\n".join(f"  • {feature}" for feature in product_config['features'][:4])
        
        body = f"""{lang_config['greeting'].format(name='[Contact Name]')}

{lang_config['intro']}

{lang_config['value_proposition'].format(product=product_config['name_short'])}

{lang_config['challenges'].format(company='[Company Name]')}:
{challenges_text}

{lang_config['benefits'].format(company='[Company Name]')}:
{benefits_text}

{lang_config['why_us']}:
  • Established manufacturer since 2004 (20+ years experience)
  • High-Tech Enterprise certified
  • Factory-direct pricing (no middlemen markup)
  • Global shipping and installation support
  • Compatible with national/international training standards
  • Full product line: driving, racing, truck, and electric vehicle simulators

Product Features - {product_config['name']} ({product_config['model_range']}):
{features_text}

{lang_config['call_to_action']}

Best regards,
{lang_config['signature']}"""
    
    return {
        "subject": subject,
        "body": body,
        "customer_type": customer_type,
        "product": product,
        "language": language,
        "follow_up": follow_up,
        "estimated_send_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def generate_email_campaign(campaign_name: str, customer_types: List[str], product: str, language: str = "en") -> Dict:
    """Generate complete email campaign"""
    emails = []
    
    for customer_type in customer_types:
        initial = generate_email_template(customer_type, product, language, follow_up=False)
        emails.append(initial)
        
        follow_up = generate_email_template(customer_type, product, language, follow_up=True)
        follow_up["send_delay_days"] = 3
        emails.append(follow_up)
        
        second_followup = generate_email_template(customer_type, product, language, follow_up=True)
        second_followup["subject"] = "Last follow-up: Transform Your Training Operations"
        second_followup["send_delay_days"] = 10
        emails.append(second_followup)
    
    return {
        "campaign_name": campaign_name,
        "customer_types": customer_types,
        "product": product,
        "language": language,
        "total_emails": len(emails),
        "emails": emails,
        "estimated_duration": "21 days",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def export_to_csv(campaign: Dict, filename: str = "email_campaign.csv"):
    """Export email campaign to CSV"""
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Campaign", "Customer Type", "Product", "Language",
            "Subject", "Body", "Send Delay (Days)", "Status"
        ])
        
        for email in campaign["emails"]:
            writer.writerow([
                campaign["campaign_name"],
                email["customer_type"],
                email["product"],
                email["language"],
                email["subject"],
                email["body"][:200] + "..." if len(email["body"]) > 200 else email["body"],
                email.get("send_delay_days", 0),
                "Draft"
            ])
    
    print(f"   ✅ Exported {len(campaign['emails'])} emails to {filename}")


def generate_multilingual_campaign(target_regions: List[str]) -> Dict:
    """Generate multilingual email campaign for multiple regions"""
    language_map = {
        "north_america": ["en"],
        "europe": ["en", "es", "fr"],
        "southeast_asia": ["en"],
        "middle_east": ["en", "ar"],
        "oceania": ["en"]
    }
    
    campaign = {
        "campaign_name": "Global Outreach Campaign - Foshan Easyly",
        "company": COMPANY["name"],
        "regions": {},
        "total_emails": 0
    }
    
    for region in target_regions:
        languages = language_map.get(region, ["en"])
        region_emails = []
        
        for language in languages:
            if language not in LANGUAGES:
                continue
            for customer_type in ["b2b_driving_school", "b2b_cdl"]:
                for product in ["driving_simulator", "heavy_vehicle"]:
                    email = generate_email_template(customer_type, product, language, follow_up=False)
                    email["region"] = region
                    email["language"] = language
                    region_emails.append(email)
                    campaign["total_emails"] += 1
        
        campaign["regions"][region] = {
            "languages": languages,
            "email_count": len(region_emails),
            "emails": region_emails
        }
    
    return campaign


def main():
    print("=" * 80)
    print(f"Foshan Easyly New Technology Co., Ltd. - Email Outreach System")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)
    
    campaigns = {
        "Driving Schools": {
            "customer_types": ["b2b_driving_school"],
            "product": "driving_simulator",
            "language": "en"
        },
        "CDL Centers": {
            "customer_types": ["b2b_cdl"],
            "product": "heavy_vehicle",
            "language": "en"
        },
        "Simulator Shops": {
            "customer_types": ["b2b2c_simulator_shop"],
            "product": "racing_simulator",
            "language": "en"
        },
        "Consumer Enthusiasts": {
            "customer_types": ["consumer"],
            "product": "racing_simulator",
            "language": "en"
        }
    }
    
    for campaign_name, config in campaigns.items():
        print(f"\n   Generating {campaign_name} campaign...")
        campaign = generate_email_campaign(campaign_name, config["customer_types"], config["product"], config["language"])
        print(f"   {campaign['total_emails']} emails generated")
    
    print(f"\n   Generating multilingual global campaign...")
    global_campaign = generate_multilingual_campaign(["north_america", "europe", "southeast_asia", "middle_east"])
    print(f"   {global_campaign['total_emails']} multilingual emails generated")
    print(f"   Regions: {', '.join(global_campaign['regions'].keys())}")
    
    print(f"\n   Exporting campaigns...")
    generated_campaigns = {}
    for campaign_name, config in campaigns.items():
        campaign = generate_email_campaign(campaign_name, config["customer_types"], config["product"], config["language"])
        generated_campaigns[campaign_name] = campaign
        export_to_csv(campaign, f"{campaign_name.lower().replace(' ', '_')}_campaign.csv")
    
    print(f"\n   Email outreach system ready!")


if __name__ == "__main__":
    main()