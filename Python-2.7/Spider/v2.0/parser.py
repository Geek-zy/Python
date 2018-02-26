#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################
# 解析器
#
#
#####################


from bs4 import BeautifulSoup
import re
import urlparse


class Parser(object):
    def _get_new_urls(self, page_url, soup):
        
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/peida/archive/*'))
        
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            #print new_full_url
            new_urls.add(new_full_url.encode('utf-8'))
            #print new_urls
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        #title_node = soup.find('a', id='cb_post_title_url')
        title_node = soup.find('div', class_='post').find('a')
        #print(title_node.get_text())
        res_data['title'] = title_node.get_text().encode('utf-8')

        #summary_node = soup.find('div', class_='post').find('p')
        #print(summary_node.get_text())
        #res_data['summary'] = title_node.get_text().encode('utf-8')

        #print res_data
        return res_data

    def parser(self, page_url, html_cont):
        
        # 判断 url 是否为空，或网页数据是否为空，为空则返回 None
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        
        return new_urls, new_data

