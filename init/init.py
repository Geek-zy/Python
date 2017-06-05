#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # 注释 
'''
    多行注释
'''

# 多变量赋值和运算
a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

a, b = b, a + b
print(a, b)

# 允许用r''表示''内部的字符串默认不转义
print(r'\n')
print('\\n')

# 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# + - * / 除法浮点 // 除法整数 % 取余
print(10 / 3)
print(10 // 3)
print(10 % 3)

# 运算符 and or not 与或非
print(True  or True)
print(True  or False)
print(False or False)

print(True  and True)
print(True  and False)
print(False and False)

print(not True)
print(not False)

