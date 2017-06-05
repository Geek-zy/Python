#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
# range()函数，可以生成一个整数序列
sum = 0
for x in range(101):
    sum = sum + x

print(sum)

# 第二种循环是while循环 while n > 0:
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2

print(sum)

# break         可以提前退出循环
# continue      跳过当前的这次循环

