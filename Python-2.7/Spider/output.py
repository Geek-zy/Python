#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################
# 输出器
#
#
#####################

class Output(object):
    def __init__(self):
    	self.datas = []

    def collect_data(self, data):
    	if data is None:
    	    return 

    	self.datas.append(data)
        #print self.datas
        #print self.datas['title']
        #print self.datas['summary']

    def output(self):
    	f = open('CSDN.html', 'w')

    	f.write('<html>')
        f.write('<meta charset="UTF-8">')
    	f.write('<body>')
    	f.write('<table>')

    	for data in self.datas:
            f.write('<tr>')
            f.write('<td><a href =%s>%s</a></td>' % (data['url'], data['url']))
            f.write('<td>%s</td>' % data['title'])
            f.write('</tr>')

    	f.write('</table')
    	f.write('</body>')
    	f.write('</html>')

    	f.close()

