#!/usr/bin/python
# -*- coding: UTF-8 -*-

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls       = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser     = html_parser.HtmlParser()
        self.outputer   = html_outputer.HtmlOutputer()

    def main(self, root_url):
        count = 1

        self.urls.add_new_url(root_url)
    
        while self.urls.has_new_url():
                
            try:
                new_url             = self.urls.get_new_url()
                print('爬虫运行状态 ==> %d : %s' % (count, new_url))
                
                #print(new_url)
                html_cont           = self.downloader.downloader(new_url)
                #print(html_cont)
                new_urls, new_data  = self.parser.parser(new_url, html_cont)
                #print(new_urls, new_data)
                
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 100:
                    break
                
                count = count + 1
            
                                
            except:
                print('爬虫爬取失败')

        self.outputer.output_html()

if __name__ == '__main__':
    
    root_url = 'http://www.cnblogs.com/peida/archive/2012/12/05/2803591.html'
    obj_spider = SpiderMain()
    obj_spider.main(root_url)

