#!/usr/bin/python3
# -*- coding: UTF-8 -*-

Key = input("请输入文件内容:")

# 打开一个文件,只写
fp = open("File.txt", "w")
fp.write(Key)

# 关闭打开的文件
fp.close()


# 打开一个文件,只读
fp = open("File.txt", "r")
G_read = fp.read()

print ("文件名称:", fp.name)
print ("是否关闭:", fp.closed)
print ("访问模式:", fp.mode)
print ("字符个数:", fp.tell())
print ("写入字符:", Key)
print ("读取字符:", G_read)

# 关闭打开的文件
fp.close()

