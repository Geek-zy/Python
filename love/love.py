#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

data = input("请输入字符:")
print('\n'.join([''.join([(data[(x-y) % len(data)] if ((x*0.05)**2 + (y*0.1)**2-1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0 else' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))

