# -*- coding: utf-8 -*-

#/home/fsg/.jumbo/lib/python2.7/site-packages/sklearn/cluster

import os

data = []
f=open("/home/fsg/jiwenchao/k_means_algorithm/data.txt", "r")

for line in f.readlines():
    line = line.rstrip()    #删除换行
    result = ' '.join(line.split())      #删除多余空格，保存一个空格连接
    s = [x for x in result.strip().split(' ')]   #字符串转换为浮点型数
    data.append(s)

#主动调用close关闭文件

f.close()


data[0]


f=open("/home/fsg/jiwenchao/new_ac_class/gbdt_model/data_set_0729.txt", "r")