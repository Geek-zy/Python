#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对list进行排序
print(sorted([36, 5, -12, 9, -21]))

# 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
# 给sorted传入key函数，即可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

