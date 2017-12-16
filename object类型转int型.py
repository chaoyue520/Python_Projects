#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 直接从数据库读取数据
data_set=os.popen(""" hive -e "select * from fangkuan_daily_data"  """)

# 直接从数据库中读取的数据多为object类型，该类型数据不影响计数count，但是sum的时候会出问题

# 解决方法，先将字段转为str型，然后再转为float或者int型等目标类型，然后再进行后续的计算处理
data_set['initialAmount']=data_set['initialAmount'].astype(str).astype(float)

data_set.groupby(['entrolment_date'])['initialAmount'].sum()