#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 安装Python包管理工具pip ==> sudo apt-get install python-pip
# 安装requests ==> pip install requests

import requests

# 调用API的GET请求
URL = "http://web.rimag.com.cn/Interfaces/Hospitalreport/fetch?hospitalId=8&pId=P00309195"
#URL = "http://web.rimag.com.cn/Interfaces/Hospitalreport/fetch"
Date = requests.get(url = URL)
#Date = requests.get(url = URL, params={'hospitalId':'8', 'pId':'P00309195'})

# 获取返回状态
print (Date.status_code)
# 获取返回URL
print (Date.url)
# 获取返回数据
print (Date.text)
# 获取返回 json 数据
print (Date.json())

