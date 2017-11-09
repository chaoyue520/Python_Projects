#!/bin/python
# -*- coding:UTF-8 -*-

data_dic=dict()

key_list=['a','b','c','d','e']
value_list=range(5)

# zip() 函数：接受多个序列作为参数，返回一个tuple
# 参考：https://www.cnblogs.com/frydsh/archive/2012/07/10/2585370.html
nvs=zip(key_list,value_list)

# 方法 1
data_dic=dict((key,value) for key,value in nvs)

# 方法 2
for i in range(5):
        data_dic[nvs[i][0]]=nvs[i][1]


# 方法 3
for item in nvs:
    data_dic[item[0]] = item[1]


print(data_dic)