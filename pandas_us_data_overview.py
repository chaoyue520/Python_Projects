#!/bin/python
# -*- coding:UTF-8 -*-
# data source : https://www.kaggle.com/kaggle/us-baby-names/data

import pandas as pd 
import numpy as np 
from collections import Counter


# load data
data=pd.read_csv('./NationalNames.csv')
data.head()
data.info()


# 将"姓名"和数量进行统计，并放入字典变量中
names_dic={}
for index,row in data.iterrows():
    if row['Name'] not in names_dic.keys():
        names_dic[row['Name']] = row['Count']
    else :
        names_dic[row['Name']] += row['Count']

name='Mary'
print '%s -> %i' %(name , names_dic.get(name))

name='Minnie'
print '%s -> %i' %(name , names_dic.get(name))

# most_common()返回list，可以使用切片操作进行选择top10或者tail10
# 首先统计最常用的名字极其count值的列表

top_10=Counter(names_dic).most_common()[0:10] #正序切片从0开始，所以0:10 表示前10个元素，index=10表示第11个元素

for pair in top_10:
    print '姓名：%s -> 数量：%i' %(pair[0],pair[1])


# 然后统计最不常用的名字极其count值的列表
tail_10=Counter(names_dic).most_common()[-10:] #逆序切片从-1开始，所以-10: 表示末尾10个元素

for pair in tail_10:
    print '姓名：%s -> 数量：%i' %(pair[0],pair[1])


# 名字的平均长度
# 统计每年男性／女性姓名的平均长度

def average_length_data_transform():
    # 按行遍历数据
    years = [] 
    # 女性姓名
    female_average_length=[]
    female_average_name_length=dict()
    
    # 男性姓名
    male_average_length=[]
    male_average_name_length=dict()
    for index,row in data.iterrows():
        # 按行遍历数据
        if row['Gender'] == 'F':
            curr_year=row['Year']
            curr_name_length=len(row['Name'])
            if curr_year not in female_average_name_length:
                # 举例说明第一条女性记录标记为：{1880:[4,1]}
                female_average_name_length[curr_year] = [curr_name_length,1]
            else :
                # 遇到第二条女性记录：{1880:[4+4,1+1]} -> {1880 : [8,2]}
                female_average_name_length[curr_year][0] += curr_name_length
                female_average_name_length[curr_year][1] += 1  
        else :
            curr_year=row['Year']
            curr_name_length=len(row['Name'])
            if curr_year not in male_average_name_length:
                # 举例说明第一条女性记录标记为：{1880:[4,1]}
                male_average_name_length[curr_year] = [curr_name_length,1]
            else :
                # 遇到第二条女性记录：{1880:[4+4,1+1]} -> {1880 : [8,2]}
                male_average_name_length[curr_year][0] += curr_name_length
                male_average_name_length[curr_year][1] += 1
    
    # 遍历处理后的字典
    # 女性
    for key, value in female_average_name_length.items():
        years.append(key)
        female_average_length.append(float(value[0])/float(value[1]))
    
    # 男性
    for key , value in male_average_name_length.items():
        years.append(key)
        male_average_length.append(float(value[0])/float(value[1]))
    
    return (female_average_length,female_average_name_length,male_average_length,male_average_name_length)


# 处理过程很长
female_average_length,female_average_name_length,male_average_length,male_average_name_length=average_length_data_transform()


# 查看结果
for year in range(1880,1891):
    print '年份：%i，总长(女)：%i，个数(女)：%i,总长(男)：%i，个数(男)：%i' %(year,female_average_name_length.get(year)[0]\
        ,female_average_name_length.get(year)[1],male_average_name_length.get(year)[0],male_average_name_length.get(year)[1])



# 建立年索引，对应的value值是每年不同姓名出现次数Count
# 举个栗子，结果如{1880：{'Lyda': 32, 'Reta': 5，……}}
top_in_each_year = dict()
years = range(1880, 2015)

for each_year in years:
    each_year_data = data[data['Year'] == each_year]
    top_in_each_year[each_year] = dict()
    for index, row in each_year_data.iterrows():            
        top_in_each_year[each_year][row['Name']] = row['Count']



# 每年Top25姓名占全年总Count的比例
all_sum = []
top_25_sum = []
for year, names_in_year in top_in_each_year.items():
    all_sum.append(sum(Counter(names_in_year).values()))
    top_25 = Counter(names_in_year).most_common(25)
    sum_temp = 0
    for pair in top_25:
        sum_temp += pair[1]
    top_25_sum.append(sum_temp)

percent_unique_names = np.array(top_25_sum).astype(float) / np.array(all_sum) * 100

# 将结果转化为list
list(percent_unique_names)



# 论美剧对新生儿名字的影响
data_named = data[(data.Name=='Rachel') & (data.Gender == 'F')]
data_named_dic={}
for index,row in data_named.iterrows():
    data_named_dic[row['Year']]=row['Count']


# 一般形式，以名字作为key，对应value是Year和Count值
friends_characters = [('Rachel','F'),('Monica','M'),('Phoebe','F'),('Ross','F'),('Chandler','F'),('Joey','F')]

for pair in friends_characters:
    data_named_dic[pair[0]]=dict()  
    # 形式：{'Monica': {}, 'Rachel': {}, 'Phoebe': {}, 'Joey': {}, 'Chandler': {}, 'Ross': {}}
    for index,row in data[(data.Name==pair[0]) & (data.Gender == pair[1])].iterrows():
        data_named_dic[pair[0]][row['Year']]=row['Count']


data_named_dic.get('Monica').get(1948)