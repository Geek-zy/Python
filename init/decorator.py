#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
def log(func):
    def wrapper(*args, **kw):
        print("call %s ():" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-05-18')

now()
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)

