#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np 

"""
输入一列字段名，逗号分隔，以列表形式读到内存中
然后把读进来的字段初始化成字典形式dic
"""

# n 等于字段的个数

def get_list(file_txt):
    fd=file(file_txt,'r')
    a=[]
    for line in fd.readlines():
        a.append(line.strip().split(','))
    b=[0]*n
    for i in range(n):
        b[i]=a[i][0]
    return b


def get_list_1(file_txt):
    fd=file(file_txt,'r')
    for line in fd.readlines():
        line.strip().split(',')
    return line.strip().split(',')


# 初始化字典
if __name__ == '__main__':
    file_txt = './xxx.txt'
    fd=file(file_txt,'r')
    n=9
    if len(fd.readlines())==1 :
        print get_list_1(file_txt)
        dic={key:[] for key in get_list_1(file_txt)}
        print dic
    else :
        print get_list(file_txt)
        dic={key:[] for key in get_list(file_txt)}
        print dic



