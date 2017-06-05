#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数，匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数lambda x: x * x实际上就是
def f(x):
    return x * x

F = lambda x: x * x
print(F)
print(F(5))

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

_F = build(1, 2)
print(_F)
print(_F())

