#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python smtp 通过MIMEText类 发送HTML格式的邮件


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pandas as pd
import numpy as np
import os

## 第一步：初始化设置

FROM = 'jiwenchao01@baidu.com'   # 发件人
TO = 'jiwenchao01@baidu.com'     # 收件人
subject = '邮件测试'              # 主题


## 第二步：构造邮件正文内容

"""
方法1：通过Python的管道函数 %s 控制邮件正文表格内容

"""

a,b,c,d=[1,2,3,4]

simi_html= """
<p><strong>Hi,all</strong></p>
<p>一、table_name_v1</p>
<table border="1">
<tr>
<th>Heading</th>
<th>Another Heading</th>
</tr>
<tr>
   <td>%s</td>
   <td>%s</td>
</tr>
<tr>
   <td>%s</td>
   <td>%s</td>
</tr>
</table>"""%(a,b,c,d)


"""
方法2：通过shell生成文件正文内容html格式

""" 

# 调用shell脚本
p=os.popen('bash /home/fsg/jiwenchao/auto_monitor_mail/ceshi.sh')
simi_html=p.read()


# 第三步：生成邮件正文，格式为 HTML
message = MIMEText(simi_html, 'HTML', 'utf-8')

message['Subject'] = Header(subject, 'utf-8')
message['From'] = FROM
message['To'] = TO


# 第四步：发送邮件
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(FROM, TO, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"



