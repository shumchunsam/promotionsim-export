#!/usr/bin/env python3
"""
ProMotion Simulators - Email Outreach System
自动生成并管理B2B/B2C开发信，支持多语言和个性化定制
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List, Optional

# 产品配置
PRODUCTS = {
    "automotive": {
        "name": "Automotive Driving Simulator",
        "name_short": "Driving Simulator",
        "description": "Professional automotive driving simulation platform for training, R&D, and entertainment",
        "features": ["3-6DOF motion platform", "Custom cockpit design", "Multi-screen display", "Force feedback steering", "Pedal integration", "VR/AR compatible"],
        "use_cases": ["Driving schools", "Driver training centers", "Automotive R&D", "Sim racing", "Therapeutic training"]
    },
    "flight": {
        "name": "Flight & Aviation Simulator",
        "name_short": "Flight Simulator",
        "description": "High-fidelity flight simulation platform for pilot training and aviation education",
        "features": ["6DOF motion platform", "Full-motion flight dynamics", "Multi-engine simulation", "Weather simulation", "ATC integration", "FAA/EASA compliant"],
        "use_cases": ["Flight schools", "Aviation universities", "Military training", "Corporate aviation", "Emergency procedure training"]
    },
    "heavy_vehicle": {
        "name": "Bus & Truck Training Simulator",
        "name_short": "Heavy Vehicle Simulator",
        "description": "Commercial vehicle simulation platform for professional driver training",
        "features": ["Heavy vehicle dynamics", "CDL preparation", "Multi-vehicle types", "Hazard perception training", "Fuel efficiency training", "DOT compliance"],
        "use_cases": ["Trucking companies", "CDL training centers", "Public transit", "Logistics companies", "Fleet training"]
    },
    "motion_platform": {
        "name": "Custom Motion Platform",
        "name_short": "Motion Platform",
        "description": "Industrial-grade multi-axis motion platform for various simulation applications",
        "features": ["3/4/6 degrees of freedom", "Custom payload capacity", "High precision actuators", "Real-time control", "Modular design", "Scalable architecture"],
        "use_cases": ["Theme parks", "VR arcades", "Research institutions", "Military simulation", "Medical training", "Amusement"]
    }
}

# 客户类型配置
CUSTOMER_TYPES = {
    "b2b_driving_school": {
        "name": "Driving School",
        "email_subjects": [
            "Transform Your Driving School with Professional Simulators",
            "Reduce Training Costs by 80% with Driving Simulators",
            "The Future of Driving Education is Here"
        ],
        "pain_points": [
            "High operational costs (fuel, insurance, maintenance)",
            "Safety concerns and liability",
            "Limited training capacity",
            "High pass-failure rates",
            "Rising regulatory costs"
        ],
        "selling_points": [
            "70-90% reduction in training costs",
            "Zero safety liability during training",
            "Unlimited training capacity",
            "Modern marketing advantage",
            "Faster driver certification"
        ],
        "call_to_action": "Schedule a free demo at your facility"
    },
    "b2b_flight_school": {
        "name": "Flight Training School",
        "email_subjects": [
            "Modernize Your Flight Training Program",
            "Reduce Aircraft Costs by 60% with Simulators",
            "FAA-EASA Compliant Flight Simulation Solutions"
        ],
        "pain_points": [
            "Aircraft operating costs",
            "Weather-related training disruptions",
            "Limited simulator availability",
            "Pilot shortage crisis",
            "Regulatory compliance costs"
        ],
        "selling_points": [
            "All-weather training capability",
            "FAA/EASA approved options",
            "Emergency procedure training",
            "Reduced aircraft wear",
            "Higher training throughput"
        ],
        "call_to_action": "Request a flight simulator quote"
    },
    "b2b_cdl": {
        "name": "CDL Training Center",
        "email_subjects": [
            "Boost CDL Pass Rates with Professional Simulators",
            "Reduce CDL Training Costs by 70%",
            "Modern CDL Training Solutions for Your School"
        ],
        "pain_points": [
            "Commercial vehicle insurance costs",
            "Federal/state compliance requirements",
            "Safety liability",
            "High maintenance costs",
            "CDL exam pass rates"
        ],
        "selling_points": [
            "Reduced insurance premiums",
            "Zero accident risk",
            "FMCSA compliance support",
            "Unlimited practice time",
            "Improved CDL pass rates"
        ],
        "call_to_action": "Get your CDL simulator quote today"
    },
    "b2b2c_simulator_shop": {
        "name": "Simulator Shop/VR Arcade",
        "email_subjects": [
            "Premium Simulators for Your Business",
            "Factory-Direct Motion Platforms for VR Arcades",
            "Upgrade Your Simulator Experience"
        ],
        "pain_points": [
            "Competition pressure",
            "Customer experience expectations",
            "Equipment upgrade costs",
            "Revenue optimization",
            "Technology differentiation"
        ],
        "selling_points": [
            "Factory-direct pricing",
            "Latest 3-6DOF technology",
            "Customization options",
            "Global shipping and installation",
            "After-sales support"
        ],
        "call_to_action": "Explore our simulator solutions"
    },
    "government": {
        "name": "Government/Defense",
        "email_subjects": [
            "Professional Simulation Solutions for Government",
            "Military-Grade Simulation Platforms",
            "Government Training Simulation Systems"
        ],
        "pain_points": [
            "Budget constraints",
            "Security requirements",
            "Training effectiveness",
            "Regulatory compliance",
            "Long-term maintenance"
        ],
        "selling_points": [
            "Military-grade quality",
            "Custom security configurations",
            "Proven government contracts",
            "Long-term support",
            "Competitive government pricing"
        ],
        "call_to_action": "Request government procurement information"
    },
    "consumer": {
        "name": "Consumer/Enthusiast",
        "email_subjects": [
            "Professional Sim Racing Platforms",
            "The Ultimate Home Simulator Experience",
            "Factory-Direct Sim Racing Rigs"
        ],
        "pain_points": [
            "Expensive pre-built rigs",
            "Limited customization",
            "Poor build quality",
            "Lack of support",
            "Upgrade difficulties"
        ],
        "selling_points": [
            "Factory-direct pricing",
            "Full customization options",
            "Premium build quality",
            "Direct manufacturer support",
            "Easy upgrades"
        ],
        "call_to_action": "Configure your custom simulator"
    }
}

# 多语言模板
LANGUAGES = {
    "en": {
        "greeting": "Dear {name},",
        "intro": "I'm reaching out from ProMotion Simulators regarding {company}'s {type} operations in {country}.",
        "value_proposition": "We specialize in professional {product} systems that directly address the challenges you face:",
        "benefits": "Key Benefits for {company}:",
        "why_us": "Why Partner With Us:",
        "challenges": "Your Current Challenges:",
        "call_to_action": "I'd love to schedule a 15-minute call to discuss how we can support your {type} training center.",
        "closing": "Best regards,",
        "signature": """Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/"""
    },
    "es": {
        "greeting": "Estimado/a {name},",
        "intro": "Le contactamos de ProMotion Simulators en relación con las operaciones de {type} en {country}.",
        "value_proposition": "Nos especializamos en sistemas profesionales de {product} que abordan directamente los desafíos que enfrenta:",
        "benefits": "Beneficios Clave para {company}:",
        "why_us": "¿Por Qué Trabajarnos?",
        "challenges": "Sus Desafíos Actuales:",
        "call_to_action": "Me encantaría programar una llamada de 15 minutos para discutir cómo podemos apoyar su centro de formación.",
        "closing": "Saludos cordiales,",
        "signature": """Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/"""
    },
    "fr": {
        "greeting": "Cher/Chère {name},",
        "intro": "Je vous contacte de ProMotion Simulators concernant les opérations de {type} en {country}.",
        "value_proposition": "Nous sommes spécialisés dans les systèmes professionnels de {product} qui répondent directement aux défis que vous affrontez:",
        "benefits": "Avantages Clés pour {company}:",
        "why_us": "Pourquoi Nous Choisir?",
        "challenges": "Vos Défis Actuels:",
        "call_to_action": "J'aimerais organiser un appel de 15 minutes pour discuter de la manière dont nous pouvons soutenir votre centre de formation.",
        "closing": "Cordialement,",
        "signature": """Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/"""
    },
    "ar": {
        "greeting": "السيد/ة {name} المحترم/ة،",
        "intro": "أتواصل معكم من ProMotion Simulators فيما يتعلق بعمليات {type} في {country}.",
        "value_proposition": "نحن متخصصون في أنظمة {product} الاحترافية التي تعالج مباشرة التحديات التي تواجهها:",
        "benefits": "الفوائد الرئيسية لـ {company}:",
        "why_us": "لماذا تختارنا؟",
        "challenges": "تحدياتكم الحالية:",
        "call_to_action": "أرغب في جدولة مكالمة لمدة 15 دقيقة لمناقشة كيفية دعم مركز التدريب الخاص بكم.",
        "closing": "مع أطيب التحيات،",
        "signature": """Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/"""
    }
}

def generate_email_template(customer_type: str, product: str, language: str = "en", follow_up: bool = False) -> Dict:
    """Generate email template for specific customer type and product"""
    customer_config = CUSTOMER_TYPES[customer_type]
    product_config = PRODUCTS[product]
    lang_config = LANGUAGES[language]
    
    if follow_up:
        subject = f"Re: {customer_config['email_subjects'][0][:60]}..."
        body = f"""{lang_config['greeting'].format(name='[Contact Name]')}

Following up on my previous email about {product_config['name']} solutions for your {customer_type.replace('_', ' ')} operations.

I wanted to share a recent success story from a {random.choice(['USA', 'Germany', 'UAE', 'Singapore', 'Australia'])} client who saw {random.choice(['40%', '60%', '70%', '80%'])} improvement in training efficiency after switching to our platform.

{lang_config['call_to_action'].format(type=customer_type.replace('_', ' '))}

{lang_config['closing']}
{lang_config['signature']}"""
    else:
        # Generate dynamic subject
        subject = random.choice(customer_config['email_subjects'])
        
        # Generate body with personalized content
        benefits = "\n".join(f"✓ {point}" for point in customer_config['selling_points'][:4])
        challenges = "\n".join(f"• {point}" for point in customer_config['pain_points'][:4])
        
        body = f"""{lang_config['greeting'].format(name='[Contact Name]')}

{lang_config['intro'].format(company='[Company Name]', type=customer_type.replace('_', ' '), country='[Country]')}

{lang_config['value_proposition'].format(product=product_config['name_short'])}

{lang_config['benefits'].format(company='[Company Name]')}:
{benefits}

{lang_config['why_us']}:
✓ Factory-direct pricing (no middlemen)
✓ Global shipping and installation support
✓ 24/7 remote technical support
✓ Customizable to your specific requirements
✓ Proven track record in {random.choice(['North America', 'Europe', 'Southeast Asia', 'Middle East', 'Oceania'])}

{lang_config['challenges'].format(company='[Company Name]')}:
{challenges}

{lang_config['call_to_action'].format(type=customer_type.replace('_', ' '))}

{lang_config['closing']}
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
        # Initial email
        initial = generate_email_template(customer_type, product, language, follow_up=False)
        emails.append(initial)
        
        # Follow-up email (3 days later)
        follow_up = generate_email_template(customer_type, product, language, follow_up=True)
        follow_up["send_delay_days"] = 3
        emails.append(follow_up)
        
        # Second follow-up (7 days later)
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
    
    print(f"✅ Exported {len(campaign['emails'])} emails to {filename}")


def generate_multilingual_campaign(target_regions: List[str]) -> Dict:
    """Generate multilingual email campaign for multiple regions"""
    language_map = {
        "north_america": ["en", "es"],
        "europe": ["en", "fr", "de", "fr"],
        "southeast_asia": ["en"],
        "middle_east": ["en", "ar"],
        "oceania": ["en"]
    }
    
    campaign = {
        "campaign_name": "Global Outreach Campaign",
        "regions": {},
        "total_emails": 0
    }
    
    for region in target_regions:
        languages = language_map.get(region, ["en"])
        region_emails = []
        
        for language in languages:
            # Generate templates for different customer types in each language
            for customer_type in ["b2b_driving_school", "b2b_flight_school", "b2b_cdl"]:
                for product in ["automotive", "flight"]:
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
    print("ProMotion Simulators - Email Outreach System")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)
    
    # Generate sample campaigns for different customer types
    campaigns = {
        "Driving Schools": {
            "customer_types": ["b2b_driving_school"],
            "product": "automotive",
            "language": "en"
        },
        "Flight Schools": {
            "customer_types": ["b2b_flight_school"],
            "product": "flight",
            "language": "en"
        },
        "CDL Centers": {
            "customer_types": ["b2b_cdl"],
            "product": "heavy_vehicle",
            "language": "en"
        },
        "Simulator Shops": {
            "customer_types": ["b2b2c_simulator_shop"],
            "product": "motion_platform",
            "language": "en"
        }
    }
    
    for campaign_name, config in campaigns.items():
        print(f"\n📧 Generating {campaign_name} campaign...")
        campaign = generate_email_campaign(campaign_name, config["customer_types"], config["product"], config["language"])
        print(f"   ✓ {campaign['total_emails']} emails generated")
        print(f"   ✓ Campaign duration: {campaign['estimated_duration']}")
    
    # Generate multilingual campaign
    print(f"\n🌍 Generating multilingual global campaign...")
    global_campaign = generate_multilingual_campaign(["north_america", "europe", "southeast_asia", "middle_east"])
    print(f"   ✓ {global_campaign['total_emails']} multilingual emails generated")
    print(f"   ✓ Regions: {', '.join(global_campaign['regions'].keys())}")
    
    # Export campaigns
    print(f"\n📁 Exporting campaigns...")
    for campaign_name in campaigns.keys():
        export_to_csv(campaigns[campaign_name], f"{campaign_name.lower().replace(' ', '_')}_campaign.csv")
    
    print(f"\n✅ Email outreach system ready!")
    print(f"📋 Next steps:")
    print(f"   1. Review email templates by customer type")
    print(f"   2. Customize content for specific regions")
    print(f"   3. Schedule email sending sequence")


if __name__ == "__main__":
    main()