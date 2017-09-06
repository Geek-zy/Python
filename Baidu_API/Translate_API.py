#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
import urllib.request
import json
import random

def Baidu_API(q):

    API = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    Appid = "20170902000079831"
    Key = "bvJrTCv3DOxa7uhxGyVL"
    httpClient = None
    fromLang = "auto"
    toLang = "auto"
    salt = random.randint(32768, 65536)
    sign = Appid + q + str(salt) + Key
    MD5 = hashlib.md5()
    MD5.update(sign.encode(encoding='utf-8'))
    sign = MD5.hexdigest()
    #q = "你好"

    API = "%s?appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s" % (API, Appid, urllib.parse.quote(q), fromLang, toLang, str(salt), sign)

    response = urllib.request.urlopen(API).read().decode('utf8')
    getJson = json.loads(response)
    getInfo = getJson['trans_result']
    re = getInfo[0]
    data = re['dst']
    data = data.replace(",", "")

    return data

if __name__ == "__main__":

    q = input("请输入要翻译的文字：")
    data = Baidu_API(q)
    print(data)

