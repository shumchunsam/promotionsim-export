#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""工程机械模拟器客户列表 - 从Alibaba搜索抓取"""

customers = [
    # 挖掘机模拟器
    {
        "company": "Maxizm Construction Machinery (Qingdao) Co., Ltd.",
        "product_type": "Excavator Simulator",
        "country": "China",
        "city": "Qingdao, Shandong",
        "contact": "Victory Xie",
        "email": "vxie@maxizm.com",
        "phone": "+86-15586567706",
        "website": "https://maxizm.en.alibaba.com",
        "products": "Road Roller, Excavator, Bulldozer, Truck Crane",
        "years_in_business": "7yrs",
        "sim_price_range": "$31,200-34,300",
        "note": "正在销售15吨挖掘机培训模拟器",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Oriemac Machinery & Equipment (Shanghai) Co., Ltd.",
        "product_type": "Excavator Simulator",
        "country": "China",
        "city": "Shanghai",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Excavator Training Simulator GE150H",
        "years_in_business": "2yrs",
        "sim_price_range": "$28,500-30,000",
        "note": "1年/2000小时保修",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Wenzhou Qiaoli Teaching Instrument Co., LTD.",
        "product_type": "Excavator Simulator",
        "country": "China",
        "city": "Wenzhou",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Static Three-Screen Excavator Simulator",
        "years_in_business": "1yr",
        "sim_price_range": "$6,000-17,900",
        "note": "静态三屏模拟器",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Jining Micro Packed Amusement Equipment Co., Ltd.",
        "product_type": "Excavator Simulator",
        "country": "China",
        "city": "Jining",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Mini Kids Electric Digger Simulator",
        "years_in_business": "9yrs",
        "sim_price_range": "$1,500-2,340",
        "note": "迷你电动挖掘机模拟器",
        "target": "6轴运动平台采购",
    },
    # 叉车模拟器
    {
        "company": "Hebei Zhongbang Mechanical Equipment Sales Co., Ltd.",
        "product_type": "Forklift Simulator",
        "country": "China",
        "city": "Hebei",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Heli Forklift 5 Ton Training Simulator",
        "years_in_business": "1yr",
        "sim_price_range": "$9,600-9,700",
        "note": "5吨叉车模拟器",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Shanghai Vostosun Industrial Co., Ltd.",
        "product_type": "Forklift Simulator",
        "country": "China",
        "city": "Shanghai",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "VSFB16F Forklift Simulator 1500kg",
        "years_in_business": "9yrs",
        "sim_price_range": "$9,600",
        "note": "1500kg叉车模拟器",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Shandong Xingke Intelligent Technology Co., Ltd.",
        "product_type": "Forklift Simulator",
        "country": "China",
        "city": "Shandong",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "VR Forklift Simulator",
        "years_in_business": "16yrs",
        "sim_price_range": "$10,000-80,000",
        "note": "VR叉车模拟器，价格跨度大",
        "target": "6轴运动平台采购",
    },
    {
        "company": "Xuzhou Longshine Intelligent Technology Co., Ltd.",
        "product_type": "Forklift Simulator",
        "country": "China",
        "city": "Xuzhou",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Virtual Reality Forklift Simulator",
        "years_in_business": "9yrs",
        "sim_price_range": "$2,999-5,999",
        "note": "VR叉车模拟器",
        "target": "6轴运动平台采购",
    },
    # 起重机模拟器
    {
        "company": "Guangzhou Naughty Dog Electronic Technology Co., Ltd.",
        "product_type": "Crane Simulator",
        "country": "China",
        "city": "Guangzhou",
        "contact": "",
        "email": "",
        "phone": "",
        "website": "",
        "products": "Claw Crane Game Machine",
        "years_in_business": "5yrs",
        "sim_price_range": "$340-350",
        "note": "抓娃娃机/起重机游戏机",
        "target": "6轴运动平台采购",
    },
]

# 保存为CSV
import csv
import os

CSV_FILE = "/home/samson/overseas_expansion/engineering_simulator_customers.csv"

with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)

print(f"Saved {len(customers)} customers to {CSV_FILE}")