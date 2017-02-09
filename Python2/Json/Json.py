#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 官网地址：http://deron.meranda.us/python/demjson/
# json安装：sudo python setup.py install

import demjson

Data_Array = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
Data_Json  = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

# 将 Python 对象编码成 JSON 字符串
print demjson.encode(Data_Array)

# 将已编码的 JSON 字符串解码为 Python 对象
print demjson.decode(Data_Json)

