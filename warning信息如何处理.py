#!/usr/bin/python
# -*- coding: UTF-8 -*-


####### 忽略所有的warnings信息


# 方法1：
import warnings
warnings.filterwarnings('ignore')


#方法2：
python -W ignore xxxx.py


# 以上两种方法均可以避免warnings的输出了，但是切记，不要盲目设置取消输出。