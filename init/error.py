#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 内置了一套try...except...finally...的错误处理机制
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕 可以没有finally
# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
try:
    print('try...')
    r = 10 / 0 
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    assert n != 0, 'n 的参数为0'
    return 10 / n

foo(1)

