#!/usr/bin/python
#-*- coding:UTF-8 -*-

import pandas as pd
import numpy as np


na_values=['','NULL','NA','null','na','Na','-9999','Infinity','NaN']
data_set_names=['bid','whitelisttype','dt_month','zxHouseLoanCnt','zxAccountCnt','zxHouseFundMonthPayAmt','reasonCode','risCode']


data_set=pd.read_table(xpath+'/zx_02.txt'
                      ,sep='\t'
                      ,na_values = na_values
                      ,header=None
                      ,names=data_set_names)


# 判断拒绝原因是否在拒绝列表中
refuse_list=['XJDE001','XJDH019','XJDR009','XJDC0080','FRG010','JXJPL007','JXJPL005','XJDH016','LBT001','LBT003','LBT004','LBT002']


# reasonCode字段是逗号分隔的str型数据，判断是否是refuse_list的子集
# 先把reasonCode字段split成列表，然后通过set()集合的形式判断是否是子集，是的话返回True
# 新增一个字段refuse_judge，当对应reasonCode字段是refuse_list子集时，对应位置是True，否则填False
# 特殊情况reasonCode字段可能是空值，所有用if判断下
# 特别说明 type(np.nan) is float 返回结果是True，所以用是否float判断字段是否是空值

refuse_judge=[]
for i in range(len(data_set)):
    if type(data_set['reasonCode'][i]) is float:
        refuse_judge.append(False)
    else:
        refuse_judge.append(set(data_set['reasonCode'][i].split(','))<set(refuse_list))


# 数据集
data_set['refuse_judge']=refuse_judge



