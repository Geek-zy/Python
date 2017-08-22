#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()

def back(i):
    print("获取鼠标当前位置：", i.x, i.y)

frame = Frame(root, width = 200, height = 200)
frame.bind("<Motion>", back)
frame.pack()

mainloop()
