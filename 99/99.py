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

