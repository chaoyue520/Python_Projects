#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
计算并输出用户指定的两个整数之间的所有素数
素数的定义是只能被1和它本身整除的数，如2,3,5,7,11等。也叫质数
"""

x=(int(input("请输入开始值(整数): ")),int(input("请输入一个结束值(整数): ")))

x1=min(x)
x2=max(x)

# 打印所有的质数
for n in range(x1,x2):
    for i in range(2,n-1):
        if n % i == 0 :
            break
    else :
        print ( n , "is prime number.");


# 打印所有的数，是质数了标记为prime number，不是质数了标记为not prime number
for n in range(x1,x2):
    for i in range(2,n-1):
        if n % i == 0 :
            print ( n , "is not prime number.")
            break
    else :
        print ( n , "is prime number.");

        
        
