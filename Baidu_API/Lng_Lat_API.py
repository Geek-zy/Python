#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import json


def BaiduSDK(data):

    API = "http://api.map.baidu.com/geocoder/v2/?output=json&ak=2.0&ak=aqEMiyyGUIux4vTfy7oDb4iq3UWmXdLY&address="
    URL = API + data
    coordinate = requests.get(url = URL).text
    coordinate = json.loads(coordinate)

    # lng 经度
    lng = str(coordinate['result']['location']['lng'])
    # lat 纬度
    lat = str(coordinate['result']['location']['lat'])

    return (lng, lat)

if __name__ == "__main__":

    data = input("请输入地名获取经纬度：")
    (lng, lat) = BaiduSDK(data)
    print("经度：%s  纬度：%s" % (lng, lat))

