#!/usr/bin/python
# -*- coding: UTF-8 -*-

class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        #print "添加新的URL" + url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        #print "批量添加新的URL" + urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)
            #print url

    def has_new_url(self):
        #print "待爬取的URL"
        return len(self.new_urls) != 0

    def get_new_url(self):
        #print "获取一个URL"
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        #print new_url
        return new_url

