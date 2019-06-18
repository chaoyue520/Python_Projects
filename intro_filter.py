#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np 


# DataFrame.filter(items=None, like=None, regex=None, axis=None)
# Subset rows or columns of dataframe according to labels in the specified index
# 返回子集


df = pd.DataFrame(np.array(([1,2,3], [4,5,6])),index=['mouse', 'rabbit'], columns=['one', 'two', 'three'])

# 按照列名筛选one和three列
df.filter(items=['one', 'three'])

# 按照列名筛选one和three列
# $ 正则表达式, e$表示以e结尾
df.filter(regex='e$', axis=1)

# ^ 正则表达式, ^t表示以t开头
df.filter(regex='^t', axis=1)

# 按照index筛选行
df.filter(like='bbi', axis=0)


# 能整除2返回False, 否则不能整除产生余数, 则返回True
def is_odd(n):
    return n%2>0

# is_odd(1) 返回True
# is_odd(2) 返回False

# 初始化一个list
numbers=[1,2,3,4,5,6,7,8]

# 返回不能奇数
odds=list(filter(is_odd,numbers))

print odds

# 运行结果
# [1,3,5,7]

# is_odd()函数 + filter的效果等同于下边filter+lambda的效果
odds = filter(lambda n: n%2>0, range(8))
lt = list(odds)
print(lt) 

# 运行结果
# [1,3,5,7]


# 备注一下, map()和filter()的区别 : filter通过生成True和False的迭代器将对象中不符合条件的元素过滤掉, 返回符合条件的元素集合
# map()是返回True或False组成的迭代器

res1 = map(lambda n: n%2>0, range(8))
lt1 = list(res1)
print lt1

# 运行结果
# [False, True, False, True, False, True, False, True]





