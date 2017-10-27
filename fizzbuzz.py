#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This program is the implementation of the famous fizzbuzz program.
If the number is divisible by both 3 and 5, then the progrma prints 'FizzBuzz'.
If the enumber is only divisible by 3, then the program prints 'Fizz'
If the enumber is only divisible by 5, then the program prints 'Buzz'

"""

def fizz_buzz(num):
    print(num)  ,   #加逗号可以把number和结果打印在同一行，print后默认有/t分隔符
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print("Number is not divisible by 3 or 5 or 15")

# 打印1~100的数字，range()函数包含起点(1)不包含终点(101)，
for i in range(1, 101):
    fizz_buzz(i)

# bingo

    
