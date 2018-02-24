#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


data = [1, 3, 5, 7, 9]

print(data)
data.append(4)
data.sort()
print(data)

i = 0
for data[i] in data:

    j = 0
    for data[j] in data:

        if data[i] < data[j]:

            t = data[i]
            data[i] = data[j]
            data[j] = t

        j += 1

    i += 1

print(data)

