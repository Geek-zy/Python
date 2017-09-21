#!/usr/bin/env python3
#-*-coding:UTF-8-*-

import time


def program_times(userMain):
    startTime = time.time()
    userMain()
    endTime = time.time()
    msecsTime = (endTime - startTime) * 1000
    print("程序运行时间：%s 毫秒" % msecsTime)

def main():
    print("程序运行开始...")
    time.sleep(0.5)
    print("程序运行结束...")

program_times(main)


def deco(userMain):
    def program_times():
        startTime = time.time()
        userMain()
        endTime = time.time()
        msecsTime = (endTime - startTime) * 1000
        print("程序运行时间：%s 毫秒" % msecsTime)
    return program_times

def main():
    print("程序运行开始...")
    time.sleep(0.5)
    print("程序运行结束...")

print("此时 main 函数的名称是：%s " % main.__name__)
main = deco(main)
print("此时 main 函数的名称是：%s " % main.__name__)
main()


def deco(userMain):
    def program_times():
        startTime = time.time()
        userMain()
        endTime = time.time()
        msecsTime = (endTime - startTime) * 1000
        print("程序运行时间：%s 毫秒" % msecsTime)
    return program_times

@deco
def main():
    print("程序运行开始...")
    time.sleep(0.5)
    print("程序运行结束...")

print("此时 main 函数的名称是：%s " % main.__name__)
main()


def deco(userMain):
    def program_times(a, b):
        startTime = time.time()
        userMain(a, b)
        endTime = time.time()
        msecsTime = (endTime - startTime) * 1000
        print("程序运行时间：%s 毫秒" % msecsTime)
    return program_times

@deco
def main(a, b):
    print("程序运行开始...")
    time.sleep(0.5)
    print("a + b = %s " % (a + b))
    print("程序运行结束...")

print("此时 main 函数的名称是：%s " % main.__name__)
main(1, 2)


def deco(text):

    def _deco(userMain):
        def program_times(*args, **kwargs):
            print(text)
            startTime = time.time()
            userMain(*args, **kwargs)
            endTime = time.time()
            msecsTime = (endTime - startTime) * 1000
            print("程序运行时间：%s 毫秒" % msecsTime)
        return program_times
    return _deco


@deco("这个是 deco 的参数")
def main(a, b, c):
    print("程序运行开始...")
    time.sleep(0.5)
    print("a + b + c = %s " % (a + b + c))
    print("程序运行结束...")

print("此时 main 函数的名称是：%s " % main.__name__)
main(1, 2, 3)


def deco_1(userMain):
    def program_times(*args, **kwargs):
        startTime = time.time()
        userMain(*args, **kwargs)
        endTime = time.time()
        msecsTime = (endTime - startTime) * 1000
        print("这里是 @deco_1 ")
        print("程序运行时间：%s 毫秒" % msecsTime)
    return program_times

def deco_2(userMain):
    def program_times(*args, **kwargs):
        startTime = time.time()
        userMain(*args, **kwargs)
        endTime = time.time()
        msecsTime = (endTime - startTime) * 1000
        print("这里是 @deco_2 ")
        print("程序运行时间：%s 毫秒" % msecsTime)
    return program_times

@deco_1
@deco_2
def main(a, b):
    print("程序运行开始...")
    time.sleep(0.5)
    print("a + b = %s " % (a + b))
    print("程序运行结束...")
main(1, 2)


class Deco(object):

    def __init__(self, var):
        super(Deco, self).__init__()
        self._var = var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, var):
        self._var = var

deco = Deco("Deco 1")
print(deco.var)

deco.var = "Deco 2"
print(deco.var)

