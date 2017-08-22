#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()

def back(i):
    print("获取鼠标点击位置：", i.x, i.y)
    Key = "获取鼠标点击位置：%d %d\n" % (i.x, i.y)
    #with open('10.txt', 'a') as fp:
        #fp.write(Key)

frame = Frame(root, width = 200, height = 200)
frame.bind("<Button-1>", back)
frame.pack()

mainloop()
