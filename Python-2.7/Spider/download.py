#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################
# 下载器
#
#
#####################

import urllib2

class Download(object):
    
    def download(self, url):

    	# 判断 URL 是否为空，为空直接返回 None
    	if url is None:
    	   return None

    	response = urllib2.urlopen(url)

    	# 判断 URL 地址是否访问成功，若失败直接返回 None
    	if response.getcode() != 200:
    	   return None

    	return response.read()
