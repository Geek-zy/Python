#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%s*%s=%s\t" % (j, i, i * j), end = '')
        j += 1
    print()
    i += 1

# 列表生成式
_list = ["%d * %d = %d" % (x, y, x*y) for x in list(range(1, 10)) for y in list(range(1, 10))]

print(_list)

