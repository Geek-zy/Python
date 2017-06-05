#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict 字典
d = {'K1': 12, 'K2': 23, 'K3': 59}
print(d)

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['K4'] = 67
print(d)
print(d['K4'])

# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value d.get('K5', -1)
print(d.get('K5', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：d.pop('K4')
d.pop('K4')
print(d)

