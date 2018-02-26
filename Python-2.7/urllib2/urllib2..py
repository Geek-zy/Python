#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2, cookielib

url = 'http://www.baidu.com'

def func_1():
    # 直接请求
    data = urllib2.urlopen(url)
    # 获取状态码 200 成功
    print(data.getcode())
    # 读取爬取内容
    print(len(data.read()))

def func_2():
    # 创建 Request 对象 
    request = urllib2.Request(url)
    # 添加数据
    #request.add_data('a', '1')
    # 添加 http 的 header
    # 将爬虫程序伪装成一个浏览器
    request.add_header('User-Agent', 'Mozilla/5.0')
    data = urllib2.urlopen(request)
    print(data.getcode())
    print(len(data.read()))

def func_3():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    data = urllib2.urlopen(url)
    print(data.getcode())
    print(data.read())

func_1()
func_2()
func_3()

