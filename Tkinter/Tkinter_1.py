#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()

def back(i):
    print("获取键盘输入字符：", repr(i.char))

frame = Frame(root, width = 200, height = 200)
frame.bind("<Key>", back)
frame.pack()
frame.focus_set()

mainloop()
