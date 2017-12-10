#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import numpy as np
import pandas as pd
import math

reload(sys)
sys.setdefaultencoding('utf-8')

input_data_file = './data.txt'

data_df = pd.read_table(input_data_file,sep = ',',na_values = ['', 'NA', 'NULL', 'na', 'null'])

# app分类统计 --------------------

# 返回item在列表li中第一次出现的index，未找到返回-1
def index(li, item):
    if len(li) > 0 and item != None:
        idxs = [i for i in range(len(li)) if li[i] == item]
        if len(idxs) > 0:
            return idxs[0]
        else: return -1
    else:
        return -1

# app分类字典
app_class_file = './app_class_by_label.txt'
app_dict = {}
app_class_set = set()
for each in open(app_class_file, 'r'):
    app_class = str(each).strip().split('\t')
    if len(app_class) > 1:
        app_dict[app_class[0]] = app_class[1]
        app_class_set.add(app_class[1]) # 注意add和update的区别、#当某类别已经在set()中存在，则add后不改变原集合数据，即集合数据不重复

app_classes = list(app_class_set)
n_app_class = len(app_classes)

# 统计每类app的安装个数
apps_list = list(data_df.erised_applist)

class_stat_ndlist = []
n_tot_apps = []
for i in range(len(apps_list)):  #对应每个人的安装app类别
	apps = str(apps_list[i]).strip().split(' ')
	n_tot_apps.append(len(apps))
	class_stat = [0] * n_app_class
	for j in range(len(apps)):
		app_cls = app_dict.get(apps[j], 'not_found')  #返回key值对应的value值
		if app_cls != 'not_found':
			idx = index(app_classes, app_cls)
			if idx != -1:
				class_stat[idx] += 1
	class_stat_ndlist.append(class_stat)


for i in range(n_app_class):
	ist_class_stat = []
	for j in range(len(apps_list)):
		ist_class_stat.append(class_stat_ndlist[j][i])
	data_df[app_classes[i]] = ist_class_stat


data_df['n_tot_apps'] = n_tot_apps

# 每类app安装占比	
app_cls = ['app_class_' + str(i) for i in range(n_app_class)]	   
for i in range(len(app_cls)):
	data_df[app_cls[i] + '_rate'] = data_df[app_cls[i]]/data_df.n_tot_apps



# 单个风险APP统计 ---------------------

# 风险app库
risk_app_file = './risk_app_set.txt'
risk_app_df = pd.read_table(risk_app_file,
							sep = '\t',
							header = None,
							names = ['var_name'])
risk_app = list(risk_app_df.var_name)
risk_app_var = ['risk_app_' + risk_app[i] for i in range(len(risk_app))]
app_dict = {}
for i in range(len(risk_app)):
	app_dict[risk_app[i]] = [0] * data_df.shape[0]

# 统计每个风险app是否安装
for i in range(len(apps_list)):
	apps = str(apps_list[i]).strip().split(' ')
	if len(apps) > 0:
		for j in range(len(apps)):
			if app_dict.get(apps[j], 'not_found') != 'not_found':
				app_dict[apps[j]][i] += 1

for i in range(len(risk_app)):
	data_df[risk_app_var[i]] = app_dict[risk_app[i]]

# 统计总的风险app安装个数及占比
data_df['cnt_risk_app'] = data_df[risk_app_var].sum(axis=1) # 按照bid维度横着相加
data_df['rate_risk_app'] = data_df.cnt_risk_app / data_df.n_tot_apps