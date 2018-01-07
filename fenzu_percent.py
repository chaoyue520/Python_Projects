#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import copy
import warnings

warnings.filterwarnings('ignore')

# load data
data=pd.read_table('result_v1.txt'
                   ,sep='\t'
                   ,header=None
                   ,names=['dt','total_bid','fraud_cnt','credit_cnt','good_cnt','other_cnt',\
                           'white_total_bid','white_fraud_cnt','white_credit_cnt','white_good_cnt','white_other_cnt',\
                           'nonwhite_total_bid','nonwhite_fraud_cnt','nonwhite_credit_cnt','nonwhite_good_cnt','nonwhite_other_cnt'])

# 计算占比
def ratio(input_data):
    output_data=copy.deepcopy(input_data)
    n=output_data.shape[0]
    for col in list(output_data.columns):
        for i in range(n):
            if col=='dt':
                output_data['dt'][i]=input_data.iloc[i][0]
            else :
                output_data[col][i]=str(round(100.0*input_data[col][i]/input_data.iloc[:,1][i],2)) + '%'
    return output_data


# 输出Total占比
data_percent=ratio(data)
data_percent.to_csv('result_v2.txt',sep='\t',header=True,index=False)


# 全量客群
data_total=data[['dt','total_bid','fraud_cnt','credit_cnt','good_cnt','other_cnt']]
v1=ratio(data_total)

# 白名单客群
data_white=data[['dt','white_total_bid','white_fraud_cnt','white_credit_cnt','white_good_cnt','white_other_cnt']]
v2=ratio(data_white)
v2=v2.drop(['dt'],axis=1)

# 非白名单客群
data_nonwhite=data[['dt','nonwhite_total_bid','nonwhite_fraud_cnt','nonwhite_credit_cnt','nonwhite_good_cnt','nonwhite_other_cnt']]
v3=ratio(data_nonwhite)
v3=v3.drop(['dt'],axis=1)

# 输出各客群占比
data_last=pd.concat([v1,v2,v3],axis=1)
data_last.to_csv('result_v3.txt',sep='\t',header=True,index=False)


