#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 多层嵌套
y=[1,2,[3,4,[5,6,7]],['a','b']]

for i in y :
    if isinstance(i,list):    #判断i是不是list类型，是返回True，否返回False
        for i_i in i :
            if isinstance(i_i,list):
                for i_i_i in i_i:
                    print i_i_i
            else :
                print i_i
    else:
        print i

# 上述代码包含重复结构，考虑构造函数来解决

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print (each_item)

# 实现嵌套for循环的效果
print_lol(y)