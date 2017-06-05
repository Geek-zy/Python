#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器

# 只要把一个列表生成式的[]改成()，就创建了一个generator
G = (x * x for x in range(10))
print(G)
for i in G:
    print(i)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    i, a, b = 0, 0, 1
    while i < max:
        print(b)
        a, b = b, a + b
        i = i + 1
    return 'done'

#fib(6)

# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
    i, a, b = 0, 0, 1
    while i < max:
        yield b
        a, b = b, a + b
        i = i + 1
    return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
f = fib(6)
print(f)

# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# generator 具有记忆功能 or 断点续传
for i in f:
    print(i)

