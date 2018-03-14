#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd 
import numpy as np 
import json
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


##########################################################
# 官方文档 : https://docs.python.org/3/library/json.html #
##########################################################

# 加载原始数据
data_set=pd.read_table('~/part1.txt'header=None,names=['id','dt','dict_jason'])

# 去除json串为空的行，并重置index()
data_set=data_set[data_set['dict_jason'].notnull()].reset_index()

# 初始化数据框
data_last=data_set[['id','dt']]

# 可用cols
cols_list=['sms_cnt', 'cell_phone_num', 'net_flow', 'total_amount']


# json_loads()函数 : 可以把json转成字典
json.loads(data_set['dict_jason'][0])

# 解析后的json串就可以像常规字典一样使用，查看数据框第一行json解析后(dict)对应的keys
json.loads(data_set['dict_jason'][0]).keys()
json.loads(data_set['dict_jason'][0]).get('code_description')



# 从某串json串中提取新的json串，并作为dataframe的新列
json_str=data_set['dict_jason']
json_str_new=[]

for i in range(len(json_str)):
    if json_str[i] is not np.nan:
        a=json_str[i].replace('\\\\"','')
        b=json.loads(a)['data'] # dict
        if b != None and json.loads(a)['data'].get('cell_behavior') and json.loads(a)['data'].get('cell_behavior')[0].get('behavior'):
            json_str_new.append(json.loads(a)['data'].get('cell_behavior')[0].get('behavior'))
        else :
            json_str_new.append(0)


data_last['json_str_new']=json_str_new


# 概览数据
data_last.head(10)



# 解析json串中第一组str
json_0=[]

for i in range(len(data_last)):
    if type(data_last['json_str_new'][i]) is not int and len(data_last['json_str_new'][i])>0:
        json_0.append(data_last['json_str_new'][i][0])
    else :
        json_0.append(0)

# 添加一列
data_last['json_0']=json_0


# 定义函数，取出对应key的value
def get_new_num(col):
    get_num=[]
    for i in range(len(data_last)):
        if type(data_last['json_0'][i]) is not int :
            get_num.append(data_last['json_0'][i].get(col))
        else :
            get_num.append(0)
    return get_num


# 提取所需key值的value
data_last['sms_cnt']=get_new_num('sms_cnt')
data_last['cell_phone_num']=get_new_num('cell_phone_num')


# 删除不需要load的数据：remove()函数或者set()函数
# a=list(set(data_last.columns))
# a.remove('dt') 
# remove也可以删除list中某个值，重点是remove没有返回值，直接在原始数据集上做修改
need_cols=list(set(data_last.columns)-set(['json_str_new','json_0']))
data_set_new=data_last[need_cols]



# 保存数据
data_set_new.to_csv('~/load_data.txt',sep='\t',header=True,index=False)