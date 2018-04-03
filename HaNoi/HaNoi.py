#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def hanoi(n, a, b, c):

    print('*** %s - %s - %s ***' % (a, b, c))
    if n == 0 :
        pass

    else:
        hanoi(n-1, a, c, b)
        print("%s -> %s" % (a, b))
        hanoi(n-1, c, b, a)

def run(n):
    print("移动 %s 层汉诺塔最少需要 %d 次" % (n, 2 ** n - 1))
    hanoi(n, 'A', 'B', 'C')

run(3)
