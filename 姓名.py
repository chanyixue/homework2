# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:24:42 2024

@author: Student
"""

def collect_user_data():
    user_data = {}
    
    user_data['name'] = input("請輸入您的姓名：")
    user_data['age'] = int(input("請輸入您的年齡："))
    user_data['height'] = float(input("請輸入您的身高（米）："))
    user_data['favorite_color'] = input("請輸入您喜愛的顏色：")
    
    return user_data

def format_user_summary(user_data):
    summary = f"{user_data['name']}, {user_data['age']}歲, 身高{user_data['height']}米, 喜愛的顏色是{user_data['favorite_color']}。"
    return summary

user_data = collect_user_data()
summary = format_user_summary(user_data)
print(summary)
