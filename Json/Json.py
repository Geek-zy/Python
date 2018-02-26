#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json

Data_Array = [{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }] 
Data_Json  = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

# 将 Python 对象编码成 JSON 字符串
print (json.dumps(Data_Array))

# 将已编码的 JSON 字符串解码为 Python 对象
print (json.loads(Data_Json))

