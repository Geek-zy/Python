#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# elif是else if的缩写，完全可以有多个elif
# 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数

s = input('输入字符串(1-3): ')
int_s = int(s)

if int_s == 1:
    print(1)

elif int_s == 2:
    print(2)

elif int_s == 3:
    print(3)

else:
    print(-1)

# if判断条件还可以简写，只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = ""
if x:
    print('True')

x = "0"
if x:
    print('True')

