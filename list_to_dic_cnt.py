#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import pandas as pd

"""
根据已知列表生成一个字典，其中key值为列表元素，value值为列表元素出现的次数
"""

# 随机生成任意字典
a_list=['a','b','c','d','a','c','r','t','i','t']

# 初始化一个空字典
dic={}


for item in a_list:
    if item not in dic.keys():
        dic[item]=1
    else :
        dic[item]=dic[item]+1

print dic

# 初始化一个列表
b_list=[]

# 计算字典中value值大于1的key值，并储存在b_list列表中
for item in dic.keys():
    if dic[key]>1:
        b_list.append(key)

print b_list


# 删除字典中满足某一类条件的key值

for item in b_list:
    del dic[item]

print dic


# 在a_list中排除b_list中的元素

#方法1：
c_list=[]
for item in a_list:
    if item not in b_list:
        c_list.append(item)

#方法2：
c_list=list(set(a_list)-set(b_list))