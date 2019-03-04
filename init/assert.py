#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    assert n != 0, 'n 的参数为0'
    return 10 / n

foo(1)

