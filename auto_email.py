#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd 
import numpy as np 
import time
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import COMMASPACE


# 定义时间变量
# time.strftime('%Y%m%d',time.localtime())
yesterday = datetime.date.today() - datetime.timedelta(days=1)
data_yest=yesterday.strftime('%Y%m%d')

# 读取数据
data_v0=os.popen((""" hive -e "SELECT * FROM test WHERE dt='%s' " """)%data_yest)



# 初始化列表
data_v1=[]
for line in data_v0.readlines():
    data_v1.append(line.strip().split('\t'))


#将数据转化成dataframe的形式
daily_data=pd.DataFrame(data_v1,columns=['bid','days','dt','amt','days_cls'])
daily_data['amt']=daily_data['amt'].astype(str).astype(float)



# 概览数据
daily_data.head()
data_subset=daily_data[['bid','dt','amt','days_cls']][daily_data.dt>='2017-05']

# 计数
data_cnt=data_subset.pivot_table(['bid'],index=['days_cls'],columns=['dt'],aggfunc='count',dropna=True)
data_cnt=data_cnt.where(data_cnt.notnull(),0).bid.astype(int)
data_cnt.to_csv('./data_cnt.txt',sep='\t',header=True,index=True)

# 求和

data_sum=data_subset.pivot_table(['amt'],index=['days_cls'],columns=['dt'],aggfunc='sum',dropna=True)
data_sum=data_sum/10000 #金额单位设置为万
data_sum=data_sum.where(data_sum.notnull(),0).amt.astype(int)
data_sum.to_csv('./data_sum.txt',sep='\t',header=True,index=True)


# 指标计算
a1=1
a2=2
a3=3


# 设置邮件正文
a=os.popen(("""
echo "<p><strong>Hi,all</strong></p>" 
echo "<p><strong>    以下是 %s 人群监控核心指标及报表:</strong></p>" 

echo "<p><strong> 一. 核心指标 </strong></p>" 
echo "<p>指标1 : %s </p> "
echo "<p>指标2 : %s </p> "
echo "<p>指标3 : %s </p> "

echo "<p><strong> 二. 客群监控 : 计数 </strong></p>" 
echo "<table border=1>" 
cat ./data_cnt.txt|awk -v a="<tr><td align=center>" -v b="</td><td align=center>" -v c="</td></tr>" -F'\t' '{print a$1b$2b$3b$4b$5b$6b$7b$8b$9c}'
echo "</table>"

echo "<p><strong> 三. 客群监控 : 求和(单位:万) </strong></p>" 
echo "<table border=1>" 
cat ./data_sum.txt|awk -v a="<tr><td align=center>" -v b="</td><td align=center>" -v c="</td></tr>" -F'\t' '{print a$1b$2b$3b$4b$5b$6b$7b$8b$9c}'
echo "</table>"
""")%(data_yest,a1,a2,a3))


#发件人，收件人，邮件主题
FROM = 'xxx@xxx'
TO = ['xxx@xxx']
subject = " 监控 - %s " %data_yest

# 
simi_html=a.read()
message = MIMEText(simi_html, 'html', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = FROM
message['TO'] = COMMASPACE.join(TO)


# 发送邮件
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(FROM, TO, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"

