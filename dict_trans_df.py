#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import pandas as pd

#python读取hive数据
new_data=os.popen(""" hive -e "use dwi ; select base_info,bank_info,account_info from risk_event where dt='20171029' limit 10;"  """)
#new_data=os.popen(""" hive -f /home/fsg/jiwenchao/non_white_cluster/xxx.sql  """)

allLines=new_data.readlines()
new_data.close()

# 初始化一个字典
key_list=['brAlsM3CellNbankAllnum','unionLoanCode1','app_shopcredit_1_5_count_success_1d']
dic={key:[] for key in key_list}


# 方法1：生成dataframe形式，先生成字典

"""
注意区分：

hive里    Null  表示空值
Python里  None  表示空值

"""


for eachline in allLines:
    a=json.loads(eachline.split('\t')[0])
    for i in range(len(key_list)):
        if key_list[i] in a.keys():
            dic[key_list[i]].append(a[key_list[i]])
        else :
            dic[key_list[i]].append(None)


# 方法2 ：生成dataframe形式，先生成字典
for eachline in allLines:
    a=json.loads(eachline.split('\t')[0])
    for key in key_list:
        if key in a.keys() :
            dic[key].append(a[key])
        else :
            dic[key].append(None)


# 然后字典转化成数据框
dic_df=pd.DataFrame.from_dict(dic,orient='columns')


# 方法3：文件写到本地，直接存储成数据框的形式
with open("result.txt","w") as file:
    for line in allLines:
        a=json.loads(line.split("\t")[0])
        for i in range(len(key_list)):
            if key_list[i] in a.keys():
                file.write(a[key_list[i]] + "\t")
            else:
                file.write(None + "\t")
        file.write("\n")


