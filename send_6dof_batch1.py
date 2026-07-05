#!/usr/bin/env python3
"""Batch 1: 6-DOF platform customers (10 emails)"""
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

customers = [
    {"name": "James Miller", "company": "SimLab Pro", "email": "james@simlabpro.com"},
    {"name": "Michael Chen", "company": "Simracing World", "email": "michael@simracingworld.com"},
    {"name": "Robert Taylor", "company": "SimSport GmbH", "email": "robert@sim-gmbh.de"},
    {"name": "Peter Johnson", "company": "The Sim Studio", "email": "peter@thesimstudio.com"},
    {"name": "David Kim", "company": "Sim Racing Depot", "email": "david@simracingdepot.com"},
    {"name": "Lucas Silva", "company": "Simulador Racing", "email": "lucas@simuladorracing.com.br"},
    {"name": "Tom Anderson", "company": "Racing Experience", "email": "tom@racingexperience.co.uk"},
    {"name": "Mark Wilson", "company": "The Sim Works", "email": "mark@thesimworks.com.au"},
    {"name": "Hiroshi Tanaka", "company": "Sim Racing Japan", "email": "hiroshi@simracing.jp"},
    {"name": "Jean Dupont", "company": "Sim Racing France", "email": "jean@simracing.fr"},
]

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 465
USERNAME = '260240751@qq.com'
AUTH_CODE = 'uaadbwnvwogrbihh'

success = 0
failed = 0

for c in customers:
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = c['email']
        msg['Subject'] = '6-DOF Racing Simulator Platform - Factory Direct from China'
        
        body = "Dear " + c['name'] + ",\n\n"
        body += "I am Samson from Foshan Easyly. We manufacture 6-DOF motion platforms\n"
        body += "for racing simulators since 2004 in Foshan, China.\n\n"
        body += "We specialize in professional 6-DOF platforms that provide:\n"
        body += "- Full 6 degrees of freedom (pitch, roll, yaw, heave, surge, sway)\n"
        body += "- Realistic acceleration and cornering forces\n"
        body += "- Up to 2000kg payload capacity\n"
        body += "- Customizable cockpit and branding options\n"
        body += "- Compatible with all major racing simulation software\n\n"
        body += "Target markets we serve:\n"
        body += "- Sim racing shops and entertainment venues\n"
        body += "- Racing simulator manufacturers\n"
        body += "- High-end consumer racing simulators\n"
        body += "- Racing driving schools\n"
        body += "- Automotive testing facilities\n\n"
        body += "Pricing: $15,000-$25,000/unit depending on specifications\n"
        body += "MOQ: 1 unit (we welcome sample orders)\n\n"
        body += "Would you like to see our 6-DOF product catalog?\n\n"
        body += "Best regards,\n"
        body += "Samson Shum\n"
        body += "Foshan Easyly New Technology Co., Ltd.\n"
        body += "Email: 260240751@qq.com\n"
        body += "WhatsApp/WeChat: +86 13798624342\n"
        body += "Website: www.studycar.com/en/\n"
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(USERNAME, AUTH_CODE)
        server.send_message(msg)
        server.quit()
        print("Sent to " + c['company'] + " (" + c['email'] + ")")
        success += 1
    except Exception as e:
        print("Failed " + c['email'] + ": " + str(e)[:60])
        failed += 1
    
    # Wait between emails to avoid rate limiting
    time.sleep(3)

print("\nBatch 1: " + str(success) + " sent, " + str(failed) + " failed")