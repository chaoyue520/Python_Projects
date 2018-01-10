
# -*- coding: utf-8 -*-

scores = [55, 80, 83, 64, 91, 100, 90, 79]

##### Python内建函数：filter
# 作用：给定一个对象序列和一个过滤函数，每个序列元素都通过过滤器函数筛选，保留函数返回为真的对象

# 函数的结果返回0或者1
def bool_func(scores):
    return scores>=80 and scores<90


# 注意：bool_func(eachline)返回的是0或1的bool型结果

def filter(bool_func,seq):
    a_seq=[]
    for eachline in seq:
        if bool_func(eachline):
            a_seq.append(eachline)
        else:
            pass
    return a_seq


# 筛选大于等于80小于90的数
print filter(bool_func,scores)


# 如果n是奇数，则返回1,否则返回0
def odd(n):
    return n%2

# 筛选所有的奇数
print filter(odd,scores)



##### Python内建函数：map
# 作用：将函数调用映射到每个序列的元素上，并返回一个含有返回值的列表
def as_float(n):
    return float(n)

# 将scores中的每个元素都转换为float型
print map(as_float,scores)


# 结合lambda函数和map函数，等价于上式
map(lambda x:float(x),scores)