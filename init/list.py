#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list 相当于数组 list中的数据类不必相同的，而array的中的类型必须全部相同。
data = ["张懿", "男", "25"]
print("list 长度:", len(data))
print(data)

# -1 最后一个元素 -2 倒数第2 -3 ......
print("最后一个元素:", data[-1])

# 往list中追加元素到末尾
data.append("程序员")
print("追加元素到末尾，新的最后一个元素:", data[-1])
print(data)

# 把元素插入到指定的位置，比如索引号为1的位置
print("初始 1 号位置元素：", data[1])
data.insert(1, "汉族")
print("把元素插入到指定的位置，比如索引号为1的位置：", data[1])
print(data)

# 删除list末尾的元素，用pop()方法
print("最后一个元素:", data[-1])
data.pop()
print("删除后最后一个元素:", data[-1])
print(data)

# 删除指定位置的元素，用pop(i)方法
print("最后指定位置元素:", data[-1])
data.pop(1)
print("删除后指定位置 1 号元素:", data[-1])
print(data)

# 元素替换
data[1] = "极客"
print(data)

# 二维list 取php s[2][1] 
s = ['python', 'java', ['asp', 'php'], 'scheme']

# 空list
NULL = []

