#!/usr/bin/env python3
"""
ProMotion Simulators - SEO Content Engine
自动生成分布式的SEO文章，用于海外社媒和博客发布
"""

import json
import os
from datetime import datetime, timedelta
import random

PRODUCTS = {
    "automotive": {
        "name": "Automotive Driving Simulator",
        "keywords": [
            "driving simulator", "car driving simulator", "automotive training simulator",
            "driving school simulator", "car driving training system", "driving instructor system"
        ],
        "longtail": [
            "how driving simulators improve driver training",
            "best driving simulator for driving schools 2025",
            "driving simulator vs real car training cost comparison",
            "automotive simulation technology for safety training"
        ],
        "audience": "Driving Schools, Driver Training Centers, Automotive Manufacturers"
    },
    "flight": {
        "name": "Flight & Aviation Simulator",
        "keywords": [
            "flight simulator", "aviation training simulator", "flight training device",
            "pilot training simulator", "flight simulation platform"
        ],
        "longtail": [
            "cost of flight simulator for pilot training",
            "flight simulator technology for aviation schools",
            "how motion platforms enhance pilot training"
        ],
        "audience": "Flight Schools, Aviation Universities, Military Training Centers"
    },
    "heavy_vehicle": {
        "name": "Bus & Truck Training Simulator",
        "keywords": [
            "truck simulator", "bus driving simulator", "commercial driving simulator",
            "CDL training simulator", "heavy vehicle simulator"
        ],
        "longtail": [
            "truck driver training simulator cost",
            "bus driving simulator for professional training",
            "commercial driver license training with simulators"
        ],
        "audience": "Trucking Companies, CDL Training Centers, Logistics Companies"
    },
    "motion_platform": {
        "name": "Custom Motion Platform",
        "keywords": [
            "motion platform", "6DOF simulator", "3DOF simulator", "motion stage",
            "multi-axis platform", "simulator platform manufacturer"
        ],
        "longtail": [
            "custom motion platform for theme parks",
            "6DOF motion simulator for VR arcades",
            "motion simulator platform for military training",
            "industrial motion platform manufacturer"
        ],
        "audience": "Theme Parks, VR Arcades, Military, Research Institutions"
    }
}

REGIONS = {
    "north_america": {
        "name": "North America",
        "keywords": ["USA", "Canada", "United States", "North America"],
        "keywords_specific": [
            "driving simulator USA", "flight simulator Canada", "driving simulator near me",
            "motion simulator North America"
        ],
        "policies": ["ADA compliance", "DOT regulations", "FAA training standards"]
    },
    "europe": {
        "name": "Europe",
        "keywords": ["EU", "Germany", "UK", "France", "Netherlands", "Scandinavia"],
        "keywords_specific": [
            "driving simulator Germany", "flight simulator UK", "driving instructor training EU",
            "motion simulator Netherlands"
        ],
        "policies": ["EU safety standards", "GDPR compliance", "CE certification"]
    },
    "southeast_asia": {
        "name": "Southeast Asia",
        "keywords": ["Thailand", "Singapore", "Malaysia", "Indonesia", "Vietnam", "Philippines"],
        "keywords_specific": [
            "driving simulator Thailand", "flight simulator Singapore",
            "driving training simulator Malaysia", "motion platform Indonesia"
        ],
        "policies": ["ASEAN standards", "local driving test requirements"]
    },
    "middle_east": {
        "name": "Middle East",
        "keywords": ["UAE", "Saudi Arabia", "Qatar", "Kuwait", "Oman", "Bahrain"],
        "keywords_specific": [
            "driving simulator UAE", "flight simulator Saudi Arabia",
            "driving training center Dubai", "motion simulator Qatar"
        ],
        "policies": ["GCC safety standards", "local driving test requirements"]
    },
    "oceania": {
        "name": "Oceania",
        "keywords": ["Australia", "New Zealand"],
        "keywords_specific": [
            "driving simulator Australia", "flight simulator New Zealand",
            "driving training simulator Perth", "motion platform Sydney"
        ],
        "policies": ["Australian road safety standards", "NZ Transport Agency requirements"]
    }
}

def generate_seo_article(product, region, lang="en"):
    """Generate a single SEO-optimized article"""
    product_info = PRODUCTS[product]
    region_info = REGIONS[region]
    
    article = {
        "title": f"The Ultimate Guide to {product_info['name']} in {region_info['name']} ({datetime.now().year})",
        "meta_description": f"Discover the best {product_info['name']} solutions in {region_info['name']}. Compare costs, features, and training benefits. Factory-direct pricing with global export.",
        "keywords": product_info['keywords'] + region_info['keywords_specific'],
        "body": f"""
# The Ultimate Guide to {product_info['name']} in {region_info['name']} ({datetime.now().year})

## Introduction
When it comes to professional {product_info['keywords'][0]} training in {region_info['name']}, the technology has advanced significantly. This comprehensive guide covers everything you need to know about {product_info['name']} solutions, from cost analysis to installation requirements.

## Why {product_info['name']}?
{product_info['name']} offers significant advantages over traditional training methods:

### Cost Efficiency
- **70-90% lower operational costs** compared to real vehicle training
- No fuel consumption, maintenance costs, or safety risks
- Unlimited practice sessions per day

### Safety First
- Zero risk of accidents during initial training
- Safe practice of emergency scenarios
- Reduced insurance liability for training centers

### Regulatory Compliance
Meeting {region_info['name']} regulatory standards including:
- {region_info['policies'][0]}
- {region_info['policies'][1]}
- Industry best practices

## Key Features to Look For
1. **High-fidelity motion platform** (3-6DOF options)
2. **Customizable cockpit design**
3. **Software compatibility** with major simulation platforms
4. **Remote maintenance support**
5. **Training curriculum integration**

## Installation & Setup
For {region_info['name']} installations, consider:
- Space requirements (typically 3x3m to 5x5m)
- Power specifications (standard 220V/110V)
- Network connectivity for software updates
- Shipping and logistics support

## Cost Analysis
The investment in a professional {product_info['keywords'][0]} varies based on:
- Motion degrees of freedom (3DOF, 4DOF, 6DOF)
- Screen/display configuration
- Software licensing
- Customization options

Factory-direct pricing starts at competitive rates with comprehensive warranty and support.

## Getting Started
Ready to upgrade your training center? Contact us for a customized quote based on your specific requirements in {region_info['name']}.

---

*Published on {datetime.now().strftime("%B %d, %Y")} | Read time: 5 minutes | Category: {product_info['name']}*
"""
    }
    
    return article


def generate_social_post(product, region, day_of_week):
    """Generate social media post"""
    product_info = PRODUCTS[product]
    region_info = REGIONS[region]
    
    hashtags = f"""#{product_info['keywords'][0]} #{product_info['name'].replace(' ', '')} 
{region_info['name'].replace(' ', '')} #{region_info['keywords'][0]}{region_info['name'].replace(' ', '')}
#{region_info['keywords'][0]}Training {datetime.now().year}"""
    
    posts = {
        "monday": f"🚀 Start your week with the future of {product_info['keywords'][0]} training!\n\nOur {product_info['name']} delivers unmatched realism for {region_info['name']} training centers. Factory-direct with global shipping.\n\n{hashtags}",
        "wednesday": f"📊 Did you know?\n\n{product_info['keywords'][0]} users report 70% faster skill acquisition compared to traditional training. Perfect for {region_info['name']} driving schools and training centers.\n\n{hashtags}",
        "friday": f"🎯 Weekend prep with {product_info['name']}!\n\nPerfect for {region_info['name']} training centers looking to scale. Book a demo today!\n\n{hashtags}"
    }
    
    return posts.get(day_of_week, posts["monday"])


def generate_lead_list():
    """Generate sample lead list for manual outreach"""
    leads = []
    
    # North America
    leads.extend([
        {"name": "DriveSolutions USA", "type": "B2B - Driving School Chain", "region": "North America", "email_pattern": "info@drivesolutions.com", "website": "https://example.com/drivesolutions", "phone": "+1-xxx-xxx-xxxx"},
        {"name": "FlightSim Academy", "type": "B2B - Flight Training School", "region": "North America", "email_pattern": "sales@flightsimacademy.com", "website": "https://example.com/flightsimacademy", "phone": "+1-xxx-xxx-xxxx"},
        {"name": "MotionSim Inc", "type": "B2C - Simulator Shop", "region": "North America", "email_pattern": "contact@motionsim.com", "website": "https://example.com/motionsim", "phone": "+1-xxx-xxx-xxxx"},
    ])
    
    # Europe
    leads.extend([
        {"name": "EuroDrive Training", "type": "B2B - Driving School Chain", "region": "Europe", "email_pattern": "info@eurodrive-training.eu", "website": "https://example.com/eurodrive", "phone": "+49-xxx-xxxxxx"},
        {"name": "London Sim Center", "type": "B2C - Simulator Shop", "region": "Europe", "email_pattern": "info@londonsim.co.uk", "website": "https://example.com/londonsim", "phone": "+44-xxx-xxxxxxx"},
        {"name": "Paris Aviation Training", "type": "B2B - Flight Training Center", "region": "Europe", "email_pattern": "contact@parisaviation.fr", "website": "https://example.com/parisaviation", "phone": "+33-xxx-xxxxxx"},
    ])
    
    # Southeast Asia
    leads.extend([
        {"name": "Bangkok Driving Academy", "type": "B2B - Driving School", "region": "Southeast Asia", "email_pattern": "info@bangkokdriving.com", "website": "https://example.com/bangkokdriving", "phone": "+66-xxx-xxxxxxx"},
        {"name": "Singapore Motion Sim", "type": "B2C - VR Arcade", "region": "Southeast Asia", "email_pattern": "sales@sgmotionsim.com", "website": "https://example.com/sgmotionsim", "phone": "+65-xxxx-xxxx"},
        {"name": "Kuala Lumpur Sim Center", "type": "B2B - Training Center", "region": "Southeast Asia", "email_pattern": "info@klsimcenter.my", "website": "https://example.com/klsimcenter", "phone": "+60-xxx-xxxxxxx"},
    ])
    
    # Middle East
    leads.extend([
        {"name": "Dubai Driving Academy", "type": "B2B - Driving School", "region": "Middle East", "email_pattern": "info@dubaidriving.ae", "website": "https://example.com/dubaidriving", "phone": "+971-xxx-xxxxxxx"},
        {"name": "Riyadh Sim Center", "type": "B2C - Simulator Shop", "region": "Middle East", "email_pattern": "sales@riyadhsim.com", "website": "https://example.com/riyadhsim", "phone": "+966-xxx-xxxxxxx"},
        {"name": "Abu Dhabi Flight Training", "type": "B2B - Flight Training Center", "region": "Middle East", "email_pattern": "info@adflighttraining.ae", "website": "https://example.com/adflighttraining", "phone": "+971-xxx-xxxxxxx"},
    ])
    
    # Oceania
    leads.extend([
        {"name": "Sydney Sim Center", "type": "B2C - Simulator Shop", "region": "Oceania", "email_pattern": "info@sydneysim.com.au", "website": "https://example.com/sydneysim", "phone": "+61-xxx-xxxxxxx"},
        {"name": "Melbourne Driving Training", "type": "B2B - Driving School", "region": "Oceania", "email_pattern": "sales@melbournedriving.com.au", "website": "https://example.com/melbournedriving", "phone": "+61-xxx-xxxxxxx"},
    ])
    
    return leads


def generate_email_template(product, region, template_type="cold"):
    """Generate email template"""
    product_info = PRODUCTS[product]
    region_info = REGIONS[region]
    
    templates = {
        "cold_b2b": f"""Subject: Elevate Your {product_info['name']} Training in {region_info['name']}

Hi [Contact Name],

I'm reaching out from ProMotion Simulators, a leading manufacturer of {product_info['name']} solutions with extensive experience serving {region_info['name']}.

We specialize in factory-direct {product_info['keywords'][0]} systems that have helped training centers in {region_info['name']} reduce operational costs by up to 80% while improving training outcomes.

Key benefits for {region_info['name']} clients:
✓ {region_info['policies'][0]} compliance
✓ {region_info['policies'][1]} standards
✓ Full training and maintenance support
✓ Global shipping with local installation support

Would you be open to a brief 15-minute call this week to discuss how we can support your {product_info['keywords'][0]} training center?

Best regards,
Samson Shum
ProMotion Simulators
https://shumchunsam.github.io/promotionsim-export/""",

        "cold_b2c": f"""Subject: The Ultimate {product_info['name']} Experience in {region_info['name']}

Hi [Contact Name],

Looking to bring the next level of {product_info['name']} experience to {region_info['name']}?

ProMotion Simulators specializes in high-performance {product_info['keywords'][0]} systems designed for entertainment venues, simulator shops, and gaming centers.

Why {region_info['name']} venues choose our {product_info['name']}:
✓ Premium build quality at factory-direct pricing
✓ Customizable for maximum customer engagement
✓ Comprehensive after-sales support
✓ Quick global shipping and installation

Visit our portfolio: https://shumchunsam.github.io/promotionsim-export/

Let me know if you'd like to discuss customization options for your {region_info['name']} location.

Best regards,
Samson Shum
ProMotion Simulators""",

        "follow_up": f"""Subject: Re: {product_info['name']} for {region_info['name']}

Hi [Contact Name],

Following up on my previous email about {product_info['name']} solutions for {region_info['name']}.

I wanted to share our latest {product_info['keywords'][0]} case study from a {region_info['name']} client who saw 40% increase in training efficiency after switching to our platform.

Would you be available for a 15-minute call next week?

Best regards,
Samson Shum
ProMotion Simulators"""
    }
    
    return templates.get(template_type, templates["cold_b2b"])


def generate_hashtag_strategy():
    """Generate hashtag strategy for social media"""
    strategy = {
        "primary_hashtags": [
            "#drivingsimulator", "#motionplatform", "#flightsimulator",
            "#3dof", "#6dof", "#simracing", "#flighttraining"
        ],
        "regional_hashtags": {
            "north_america": ["#USAdriving", "#CanadaTraining", "#NorthAmericaSim"],
            "europe": ["#EuroDriving", "#UKTraining", "#GermanDriving", "#FSDriving"],
            "southeast_asia": ["#ThaiDriving", "#SGTraining", "#MalaysiaSim", "#IndonesiaSim"],
            "middle_east": ["#UAEDriving", "#SaudiTraining", "#QatarSim", "#DubaiSim"],
            "oceania": ["#AusDriving", "#NZTraining", "#OceaniaSim"]
        },
        "business_hashtags": [
            "#B2Bsimulator", "#drivingschool", "#pilottraining",
            "#commercialdriving", "#simulatorplatform", "#factorydirect"
        ],
        "trending_hashtags": [
            f"{datetime.now().year}Training", "#VRsimulator", "#immersivelearning",
            "#safetytraining", "#protrainingsim"
        ]
    }
    
    return strategy


def main():
    print("=" * 60)
    print("ProMotion Simulators - Content Engine")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    # Generate SEO articles
    print("\n📝 Generating SEO Articles...")
    for product in PRODUCTS.keys():
        for region in REGIONS.keys():
            article = generate_seo_article(product, region)
            print(f"  ✓ {article['title'][:50]}...")
    
    # Generate social media posts
    print("\n📱 Generating Social Media Posts...")
    for product in PRODUCTS.keys():
        for region in REGIONS.keys():
            post = generate_social_post(product, region, "monday")
            print(f"  ✓ {product} - {region} post")
    
    # Generate lead list
    print("\n📋 Generating Lead List...")
    leads = generate_lead_list()
    print(f"  ✓ {len(leads)} sample leads generated")
    
    # Generate email templates
    print("\n📧 Generating Email Templates...")
    for product in PRODUCTS.keys():
        for region in REGIONS.keys():
            for template_type in ["cold_b2b", "cold_b2c", "follow_up"]:
                template = generate_email_template(product, region, template_type)
                print(f"  ✓ {product} - {region} - {template_type}")
    
    # Generate hashtag strategy
    print("\n🏷️ Generating Hashtag Strategy...")
    strategy = generate_hashtag_strategy()
    print(f"  ✓ Primary hashtags: {len(strategy['primary_hashtags'])}")
    print(f"  ✓ Regional hashtags: {sum(len(v) for v in strategy['regional_hashtags'].values())}")
    print(f"  ✓ Business hashtags: {len(strategy['business_hashtags'])}")
    
    print("\n" + "=" * 60)
    print("✅ Content engine ready!")
    print("=" * 60)


if __name__ == "__main__":
    main()