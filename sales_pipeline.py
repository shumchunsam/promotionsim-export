#!/usr/bin/env python3
"""
Foshan Easyly - Complete Sales Pipeline Management
自动管理销售漏斗，从潜在客户到成交的全流程跟踪
"""

import json
import os
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Optional


# 销售阶段定义
SALES_STAGES = {
    "prospect": "新线索",
    "contacted": "已联系",
    "interested": "感兴趣",
    "demo": "演示安排",
    "quote": "报价中",
    "negotiation": "谈判中",
    "proposal": "提案已发",
    "won": "成交",
    "lost": "丢失"
}

# 客户类型配置
CUSTOMER_TYPES = {
    "driving_school": {
        "name": "Driving School",
        "email_template": "driving_school",
        "avg_deal_size": 15000,
        "sales_cycle_days": 30,
        "key_pain_points": [
            "High fuel costs",
            "Safety liability",
            "Low pass rates",
            "Limited capacity"
        ],
        "key_benefits": [
            "70% fuel cost reduction",
            "Zero accident liability",
            "24/7 training availability",
            "40% faster training"
        ]
    },
    "cdl_center": {
        "name": "CDL Training Center",
        "email_template": "cdl",
        "avg_deal_size": 80000,
        "sales_cycle_days": 45,
        "key_pain_points": [
            "High training costs",
            "Compliance requirements",
            "Driver shortage",
            "Safety concerns"
        ],
        "key_benefits": [
            "70% cost reduction",
            "Full compliance support",
            "Faster driver training",
            "Zero accident risk"
        ]
    },
    "government": {
        "name": "Government/Defense",
        "email_template": "government",
        "avg_deal_size": 250000,
        "sales_cycle_days": 90,
        "key_pain_points": [
            "Budget constraints",
            "Compliance requirements",
            "Long-term support needs",
            "Security concerns"
        ],
        "key_benefits": [
            "Certified High-Tech Enterprise",
            "Full documentation support",
            "24/7 maintenance",
            "Proven track record"
        ]
    },
    "sim_racing_shop": {
        "name": "Sim Racing Shop",
        "email_template": "simulator_shop",
        "avg_deal_size": 25000,
        "sales_cycle_days": 21,
        "key_pain_points": [
            "Competition pressure",
            "Customer experience",
            "Equipment costs",
            "Maintenance issues"
        ],
        "key_benefits": [
            "60% cheaper than Western brands",
            "Latest 6-DOF technology",
            "Full installation support",
            "After-sales warranty"
        ]
    }
}


class SalesPipeline:
    """销售漏斗管理类"""
    
    def __init__(self, data_file: str = "sales_pipeline.json"):
        self.data_file = data_file
        self.leads: List[Dict] = []
        self.load_data()
    
    def load_data(self):
        """加载数据"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.leads = json.load(f)
        else:
            self.leads = []
    
    def save_data(self):
        """保存数据"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.leads, f, indent=2, ensure_ascii=False)
    
    def add_lead(self, name: str, company: str, country: str, 
                 email: str, phone: str, customer_type: str,
                 status: str = "prospect", notes: str = ""):
        """添加新线索"""
        lead = {
            "id": len(self.leads) + 1,
            "name": name,
            "company": company,
            "country": country,
            "email": email,
            "phone": phone,
            "customer_type": customer_type,
            "status": status,
            "notes": notes,
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "last_contact": None,
            "next_followup": None,
            "deal_size": CUSTOMER_TYPES.get(customer_type, {}).get("avg_deal_size", 10000),
            "stage_history": [{"stage": status, "date": datetime.now().strftime("%Y-%m-%d")}]
        }
        self.leads.append(lead)
        self.save_data()
        print(f"✓ Added new lead: {name} from {company}")
        return lead
    
    def update_status(self, lead_id: int, new_status: str):
        """更新线索状态"""
        for lead in self.leads:
            if lead["id"] == lead_id:
                old_status = lead["status"]
                lead["status"] = new_status
                lead["last_contact"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # 记录阶段变化
                lead["stage_history"].append({
                    "stage": new_status,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "from": old_status
                })
                
                # 计算下次跟进时间
                customer_type = lead.get("customer_type", "driving_school")
                cycle_days = CUSTOMER_TYPES.get(customer_type, {}).get("sales_cycle_days", 30)
                lead["next_followup"] = (datetime.now() + timedelta(days=cycle_days)).strftime("%Y-%m-%d")
                
                self.save_data()
                print(f"✓ Updated lead {lead_id}: {old_status} → {new_status}")
                return lead
        print(f"✗ Lead {lead_id} not found")
        return None
    
    def add_note(self, lead_id: int, note: str):
        """添加备注"""
        for lead in self.leads:
            if lead["id"] == lead_id:
                if not lead["notes"]:
                    lead["notes"] = note
                else:
                    lead["notes"] += f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {note}"
                self.save_data()
                print(f"✓ Added note to lead {lead_id}")
                return True
        print(f"✗ Lead {lead_id} not found")
        return False
    
    def get_pipeline_report(self) -> Dict:
        """生成销售漏斗报告"""
        report = {
            "total_leads": len(self.leads),
            "by_status": {},
            "by_type": {},
            "by_country": {},
            "total_pipeline_value": 0,
            "recent_activity": []
        }
        
        # 按状态统计
        for lead in self.leads:
            status = lead["status"]
            report["by_status"][status] = report["by_status"].get(status, 0) + 1
            
            # 按类型统计
            ctype = lead.get("customer_type", "unknown")
            report["by_type"][ctype] = report["by_type"].get(ctype, 0) + 1
            
            # 按国家统计
            country = lead.get("country", "unknown")
            report["by_country"][country] = report["by_country"].get(country, 0) + 1
            
            # 计算管道价值
            report["total_pipeline_value"] += lead.get("deal_size", 0)
            
            # 最近活动
            if lead.get("last_contact"):
                report["recent_activity"].append({
                    "lead": lead["name"],
                    "action": f"Contacted: {lead['status']}",
                    "date": lead["last_contact"]
                })
        
        # 按时间排序最近活动
        report["recent_activity"].sort(key=lambda x: x["date"], reverse=True)
        report["recent_activity"] = report["recent_activity"][:10]
        
        return report
    
    def get_followup_list(self) -> List[Dict]:
        """获取需要跟进的线索列表"""
        today = datetime.now().strftime("%Y-%m-%d")
        followups = []
        
        for lead in self.leads:
            if lead.get("next_followup") and lead["next_followup"] <= today:
                if lead["status"] not in ["won", "lost"]:
                    followups.append(lead)
        
        return followups


def generate_pipeline_template():
    """生成销售漏斗模板"""
    pipeline = SalesPipeline()
    
    # 添加示例线索
    pipeline.add_lead(
        "John Smith",
        "AAA Driving Academy",
        "USA",
        "john@aaadriving.com",
        "+1-555-0123",
        "driving_school",
        "contacted",
        "Initial contact via LinkedIn. Interested in YSL2021-86 model."
    )
    
    pipeline.add_lead(
        "Ahmed Al-Rashid",
        "RTA Dubai Training",
        "UAE",
        "ahmed@rta.gov.ae",
        "+971-50-123-4567",
        "government",
        "prospect",
        "Government project for Vision 2030 training program."
    )
    
    pipeline.add_lead(
        "Sarah Johnson",
        "DriveWise Canada",
        "Canada",
        "sarah@drivewisecanada.com",
        "+1-416-555-0199",
        "driving_school",
        "interested",
        "Met at driving school expo. Requested quotation for 5 units."
    )
    
    pipeline.add_lead(
        "Carlos Martinez",
        "SimRacing España",
        "Spain",
        "carlos@simracingspain.com",
        "+34-612-345-678",
        "sim_racing_shop",
        "quote",
        "Want 6-DOF platforms for entertainment venue. Need custom branding."
    )
    
    print("Template pipeline created with 4 sample leads")
    return pipeline


def generate_weekly_report(pipeline: SalesPipeline):
    """生成周报"""
    report = pipeline.get_pipeline_report()
    
    print("\n" + "="*80)
    print("FOSHAN EASYLY - WEEKLY SALES PIPELINE REPORT")
    print("="*80)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Total Leads: {report['total_leads']}")
    print(f"Pipeline Value: ${report['total_pipeline_value']:,.2f}")
    
    print("\nBy Status:")
    for status, count in sorted(report["by_status"].items()):
        stage_name = SALES_STAGES.get(status, status)
        print(f"  {stage_name}: {count}")
    
    print("\nBy Customer Type:")
    for ctype, count in sorted(report["by_type"].items()):
        type_name = CUSTOMER_TYPES.get(ctype, {}).get("name", ctype)
        print(f"  {type_name}: {count}")
    
    print("\nBy Country:")
    for country, count in sorted(report["by_country"].items()):
        print(f"  {country}: {count}")
    
    print("\nRecent Activity:")
    for activity in report["recent_activity"][:5]:
        print(f"  [{activity['date']}] {activity['lead']}: {activity['action']}")
    
    # 获取需要跟进的列表
    followups = pipeline.get_followup_list()
    if followups:
        print(f"\n⚠️  Need Follow-up: {len(followups)} leads")
        for lead in followups[:5]:
            print(f"  - {lead['name']} ({lead['company']}) - {lead['status']}")
    
    print("\n" + "="*80)


def main():
    print("="*80)
    print("Foshan Easyly - Sales Pipeline Management System")
    print("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("="*80)
    
    # 生成模板数据
    pipeline = generate_pipeline_template()
    
    # 生成周报
    generate_weekly_report(pipeline)
    
    # 展示操作示例
    print("\n--- USAGE EXAMPLES ---")
    print("\n1. Add new lead:")
    print("   pipeline.add_lead('Name', 'Company', 'Country', 'email', 'phone', 'type')")
    
    print("\n2. Update lead status:")
    print("   pipeline.update_status(1, 'interested')")
    
    print("\n3. Add note:")
    print("   pipeline.add_note(1, 'Customer wants 5 units with custom branding')")
    
    print("\n4. Get pipeline report:")
    print("   report = pipeline.get_pipeline_report()")
    
    print("\n5. Get follow-up list:")
    print("   followups = pipeline.get_followup_list()")


if __name__ == "__main__":
    main()