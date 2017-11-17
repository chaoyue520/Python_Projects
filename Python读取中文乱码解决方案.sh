#!/bin/bash

# 确认当前机器编码形式，如果不是zh_CN.utf-8，则无法正确读取中文
echo $LANG

# 需要在执行Python脚本的那台机器上修改输出文档编码形式
export LANG=zh_CN.utf-8

python send_hi.py


# send_hi.py内容

pd.read_table('./b.txt')

# b.txt内容
今天
天气
好
晴朗