#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np 

"""
����һ���ֶ��������ŷָ������б���ʽ�����ڴ���
Ȼ��Ѷ��������ֶγ�ʼ�����ֵ���ʽdic
"""

# n �����ֶεĸ���

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


# ��ʼ���ֵ�
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



