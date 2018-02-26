#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################
# 管理器
#
#
#####################

class Manager(object):

    def __init__(self):

        # 待爬取的 URL 集合
        self.new_urls = set()
        # 已爬取的 URL 集合
        self.old_urls = set()

    # 新添加的 URL
    def add_new_url(self, url):

        # 判断 url 是否为空，为空则返回 None
        if url is None:
            return

        # 判断 url 是否存在于【待爬取的 URL 集合】和【已爬取的 URL 集合】，如若都不在将新 url 添加到【待爬取的 URL 集合】中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量新添加的 URL
    def add_new_urls(self, urls):
 
        if urls is None or len(urls) == 0:
            return
 
        for url in urls:
            self.new_urls.add(url)

    # 返回管理器中 URL 的数量
    def has_new_url(self):

        return len(self.new_urls) != 0

    # 从管理器中获取一个 URL
    def get_new_url(self):

        # 
        url = self.new_urls.pop()
        self.old_urls.add(url)

        return url

