#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################
# 调度器
#
#
#####################

import manager, download, parser, output


class Spider(object):

    def __init__(self):

        # 实例化 管理器、下载器、解析器、输出器
        self.manager  = manager.Manager()
        self.download = download.Download()
        self.parser   = parser.Parser()
        self.output   = output.Output()

    def spider(self, url):

        # 爬虫计数器
        count = 0

        # 将第一个 URL 放入管理器中
        self.manager.add_new_url(url)
    
        # 判断管理器中 URL 的数量是否为 0
        while self.manager.has_new_url():
                
            try:
                
                # 从管理器中获取一个 URL
                new_url = self.manager.get_new_url()
                
                # 将获取到的 URL 交给下载器处理
                html_cont = self.download.download(new_url)
                
                # 将 URL 和 下载器处理后的网页数据交给解析器处理
                new_manager, new_data = self.parser.parser(new_url, html_cont)
                
                # 将解析器处理后的数据和新的 URL 分别交给管理器和输出器
                self.manager.add_new_urls(new_manager)
                self.output.collect_data(new_data)
                
                # 爬取 100 次
                if count == 10:
                    break
                
                count += 1
            
                print('爬虫运行状态 ==> %d : %s' % (count, new_url))
                                
            except:

                print('爬虫爬取失败')

        # 当爬虫爬取完所有数据后，输出器将数据输出到文件
        self.output.output()

if __name__ == '__main__':
    
    # URL 入口（爬虫爬取的第一个 URL）
    url = 'http://www.cnblogs.com/peida/archive/2012/12/05/2803591.html'
    
    # 实例化调度器并启动爬虫
    run = Spider()
    run.spider(url)
