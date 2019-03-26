#!/usr/bin/env
# -*- coding:utf-8 -*-


# dict字典里面的(key, value)  pairs是无序的
# 但是使用ordereddict可以创建有顺序的字典
# 但是会比较耗时
# 简而言之, ordereddict提供了一种有序的dict结构


from collections import OrderedDict

# case 1 : 创建一个字典
d = dict([('a', 1), ('b', 2), ('c', 3)])

print d

# 结果 {'a': 1, 'c': 3, 'b': 2}

# case 2 : 通过OrderedDict创建字典
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print od.keys()
print od.values()

# 结果 ['a', 'b', 'c']  [1,2,3] 顺序跟创建的时候一致


# case 3 :

od=OrderedDict()
od['z']=1
od['y']=2
od['x']=3

print od.keys()

# 结果 : ['z', 'y', 'x'] 跟创建时的顺序一致




