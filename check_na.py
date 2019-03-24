#!/usr/bin/python
#-*- coding:utf-8 -*-


# count()函数 : Count non-NA cells for each column or row.
# axis : {0 or ‘index’, 1 or ‘columns’}, default 0
def check_na(df):
    print df.count(axis=0)



# 数据集data_set, 返回每列中空值的数量
check_na(data_set)

