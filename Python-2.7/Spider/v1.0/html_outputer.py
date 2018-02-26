#!/usr/bin/python
# -*- coding: UTF-8 -*-

class HtmlOutputer(object):
    def __init__(self):
    	self.datas = []

    def collect_data(self, data):
    	if data is None:
    	    return 

    	self.datas.append(data)
        #print self.datas
        #print self.datas['title']
        #print self.datas['summary']

    def output_html(self):
    	f = open('baike.html', 'w')

    	f.write('<html>')
        f.write('<meta charset="UTF-8">')
    	f.write('<body>')
    	f.write('<table>')

    	for data in self.datas:
            f.write('<tr>')
            f.write('<td><a href =%s>%s</a></td>' % (data['url'], data['url']))
            f.write('<td>%s</td>' % data['title'])#.encode('utf-8'))
            #f.write('<td>%s</td>' % data['summary'])#.encode('utf-8'))
            f.write('</tr>')

    	f.write('</table')
    	f.write('</body>')
    	f.write('</html>')

    	f.close()

