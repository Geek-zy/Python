#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def f(x):
    return x * x

data = map(f, L)
print(list(data))
# map 其实就是把函数的指针和一个数组指针传入，从而计算数组的操作

# 将list所有数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

