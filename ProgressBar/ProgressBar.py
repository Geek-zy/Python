#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time


def progress_bar(num):

    j = "#"; k = "="; t = "|/-\\"; #s = " " * (num + 1)

    for i in range(0, num + 1):

        j += "#"; k += "="; s = ("=" * i) + (" " * (num - i))
        
        #print(int(i/num*100), end='%\r')
        #print('%.2f' % (i/num*100), end='%\r')
        #print('%.2f' % (i*100/num), end='%\r')
        #print('complete percent:', time.strftime("%Y-%m-%d %H:%M:%S", \
        #        time.localtime()), int((i/num)*100), end='%\r')
        #print(str(int(i/num*100)) + '% ' + j + '->', end='\r')
        #print(k + ">" + str(int(i/num*100)), end='%\r')
        #print("[%s]" % t[i%4], end='\r')
        #print("[%s][%s][%.2f" % (t[i%4], k, (i/num*100)), "%]", end='\r')
        print("[%s][%s][%.2f" % (t[i%4], s, (i/num*100)), "%]", end='\r')

        time.sleep(0.1)

    print()

progress_bar(32)


'''
# 除了自己实现以外，Python 还提供了Tqdm 模块
# Tqdm 是一个快速、扩展性强的进度条工具库，它提供了非常多的接口，有兴趣的小伙伴可以了解一下
# GitHub 地址是：https://github.com/tqdm/tqdm
# 我们来看下，如何使用 Tqdm 模块来实现进度条
# 首先是安装：pip install tqdm
'''
#from tqdm import tqdm
#for i in tqdm(range(1, 500)):
#    sleep(0.01)

