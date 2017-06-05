#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环太繁琐，而列表生成式则可以用一行语句代替循环
_list = [x * x for x in range(1, 11)]
print(_list)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
_list = [x * x for x in range(1, 11) if x % 2 == 0]
print(_list)

# 使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']
print(_list)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
_list = [k + '=' + v for k, v in d.items()]
print(_list)

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
_list = [s.lower() for s in L]
print(_list)

# 内建的isinstance函数可以判断一个变量是不是字符串
L = ['Hello', 'World', 18, 'Apple', None]
_list = [s.lower() for s in L if isinstance(s, str) == True]
print(_list)

