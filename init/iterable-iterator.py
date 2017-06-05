#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象

# 使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

