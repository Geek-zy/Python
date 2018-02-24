#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random


while True:

    four = lambda :random.choice(['+', '-', '*', '/'])
    data = lambda :random.choice(range(1, 21))

    algo = "%d %s %d %s %d %s %d" % (data(), four(), data(), four(), data(), four(), data())

    if eval(algo) == 24:
        print(algo)
        break
