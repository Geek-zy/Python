#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time

def program_times(key = 'ms'):
    
    if key == 'ms':
        def _program_times(userMain):
            def main(*args, **kw):
                startTime = time.time()
                userMain()
                endTime = time.time()
                msecsTime = (endTime - startTime) * 1000
                print(msecsTime)
            return main

    elif key == 's':
        def _program_times(userMain):
            def main(*args, **kw):
                startTime = time.time()
                userMain()
                endTime = time.time()
                msecsTime = (endTime - startTime)
                print(msecsTime)
            return main

    elif key == 'm':
        def _program_times(userMain):
            def main(*args, **kw):
                startTime = time.time()
                userMain()
                endTime = time.time()
                msecsTime = (endTime - startTime) / 60
                print(msecsTime)
            return main

    elif key == 'h':
        def _program_times(userMain):
            def main(*args, **kw):
                startTime = time.time()
                userMain()
                endTime = time.time()
                msecsTime = (endTime - startTime) / 3600
                print(msecsTime)
            return main

    else:
        def _program_times(userMain):
            def main(*args, **kw):
                print("请正确输入参数：默认为毫秒 | 毫秒 ==> ms | 秒 ==> s | 分钟 ==> m | 小时 ==> h |")
            return main
    
    return _program_times


@program_times('s')
def Geek():
    time.sleep(1)

Geek()

