#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np 


data_set=pd.pandas

df1=pd.DataFrame(np.random.randn(4,5),index=list('ABCD'),columns=list('ABCDE'))
df1.columns=['A1','A2','B1','B2','B3']


# 过滤B开头的列, 并按列求和
df1.filter(regex='B.*').sum(1)

# 新增一列, 储存B开头列的和
df1['sum_B']=df1.filter(regex='B.*').sum(1)