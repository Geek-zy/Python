#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python引入了with语句来自动帮我们调用close()方法
# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
# r 读 rb 读取二进制文件 
# 标识符'w'或者'wb'表示写文本文件或写二进制文件
# 反复调用read() 来读取文件
# 反复调用write()来写入文件
with open('map.py', 'r') as f:
    print(f.read())

# 数据读写不一定是文件，也可以在内存中读写
# StringIO顾名思义就是在内存中读写str
# getvalue()方法用于获得写入后的str
from io import StringIO

# 写入内存
f = StringIO()
f.write('Hello Word!')
print(f.getvalue())

# 读取内存
f = StringIO('Hello Word!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO实现了在内存中读写bytes
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

import os 

# 执行结果 0或者1
x = os.system('ls')
print(x)

y = os.popen('ls')
print(y)
y.close()

