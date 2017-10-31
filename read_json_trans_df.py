#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import pandas as pd


########################################################### 第一步：初始化 dic 

# 方法1： 直接删除换行符，函数 rstrip，strip，split
def get_list(file_txt):
    fd=file(file_txt,'r')
    a=[]
    for line in fd.readlines():
        line = line.rstrip('')   #删除换行
        result = ' '.join(line.split(','))      #删除多余空格，保存一个空格连接
        s = [x for x in result.strip().split(' ')]   #字符串转换为浮点型数
        a.append(s[0])
    return a

key_list=get_list('/home/fsg/jiwenchao/non_white_cluster/col_list.txt')
dic={key:[] for key in key_list}


# 方法2 ： 初始化所以字段列表
def get_list(file_txt,n):
    fd=file(file_txt,'r')
    a=[]
    for line in fd.readlines():
        a.append(line.strip('\r\n').strip('').split(','))
    b=[0]*n
    for i in range(n):
        b[i]=a[i][0]
    return b


# 读取字段个数，并转化成整型
f=os.popen(" wc -l '/home/fsg/jiwenchao/non_white_cluster/col_list.txt' ")
n=int(f.readline().strip().split(' ')[0])

# 读取字段，并存储为列表形式
key_list=get_list('/home/fsg/jiwenchao/non_white_cluster/col_list.txt',n)

# 把列表字段初始化为一个字典表
dic={key:[] for key in key_list}


########################################################### 第二步：读取数据 

# 读取hive数据
new_data=os.popen(""" hive -e "use dwi ; select base_info,dt from risk_event where dt = '20171029'  limit 10;"  """)
#new_data=os.popen(""" hive -f /home/fsg/jiwenchao/non_white_cluster/xxx.sql  """)

#json串转化为字典形式
allLines=new_data.readlines()
new_data.close()

# 时间标签dt不在json串中，可以通过else添加时间标签 dt
# 如果是多个json串，可以考虑生成两个dict，根据逐渐在join在一起
for eachline in allLines:
    a=json.loads(eachline.split('\t')[0])
    b=json.loads(eachline.split('\t')[1])
    for key in key_list : 
        if key in a.keys() :
            dic[key].append(a[key])
        else :
            dic[key].append(None)
            dic['dt'] = b


########################################################### 第三步：json 转 DataFrame 

dic_data=pd.DataFrame.from_dict(dic,orient='columns')


