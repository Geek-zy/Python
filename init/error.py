#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python 内置了一套 try...except...else...finally 的错误处理机制

# 当我们认为某些代码可能会出错时，就可以用 try 来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即 except 语句块，执行完 except 后，如果有 finally 语句块，则执行 finally 语句块，至此，执行完毕可以没有 finally

# 此外，如果没有错误发生，可以在 except 语句块后面加一个 else，当没有错误发生时，会自动执行 else 语句

try:
    print('try...\n')
    r = 10 / 1

except ZeroDivisionError as e::
    print('except...\n')

else:   
    print('else...\n')

finally:
    print('finally...\n')

print('END')

