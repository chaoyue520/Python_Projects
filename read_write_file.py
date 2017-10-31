#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# 随机生成数据框
df = pd.DataFrame({'a':[np.NaN,np.NaN,'9','23.68','24.59'],
                   'b':[11,1.52,11,81,3.61123],
                   'c':['F','M','F','F',np.NaN],
                   'd':[90,32,32,np.NaN,np.NaN],
                   'e':[1.0,np.NaN,40.0,np.NaN,9.1],
                   'f':[1,1,0,1,1],
                    'g':['北京','天津','兰州','重庆',np.NaN] })


"""
Tips：

1、i 控制行，所以 i 每次取值循环结束后，需要f.write('\n') 换行
2、j 控制每行的列元素，特定行，某个j元素写入后，要以 '\t' 结尾，即 f.write(str(df.iloc[i][j])+'\t')

"""

# 首先定义输出文件的列名
header = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

with open('test.txt','wt') as f:
    f.write('\t'.join(header)+'\n')
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            f.write(str(df.iloc[i][j])+'\t')
        f.write('\n')


### 复杂一点

# 需要写入的数据来源于两个数据结构，相当于写入两个文件拼接后的文件

df = pd.DataFrame({'a':[np.NaN,np.NaN,'9','23.68','24.59'],
                   'b':[11,1.52,11,81,3.61123],
                   'c':['F','M','F','F',np.NaN],
                   'd':[90,32,32,np.NaN,np.NaN],
                   'e':[1.0,np.NaN,40.0,np.NaN,9.1],
                   'f':[1,1,0,1,1],
                    'g':['北京','天津','兰州','重庆',np.NaN] })


y_label=range(1,10,2)


# 首先定义输出文件的列名
header = ['a', 'b', 'c', 'd', 'e', 'f', 'g','y_label']


# 第i行写完后需要换行了。在换行前，写入y_label的数据，然后再换行，即把y_label的数据写在每一行(i)的末尾
with open('test.txt','wt') as f:
    f.write('\t'.join(header)+'\n')
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            f.write(str(df.iloc[i][j])+'\t')
        f.write(str(y_label[i])+'\n')


