#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def api(app):

    def application(environ, start_response):

        start_response('200 OK', [('Content-Type', 'text/html')])
        parse = parse_qs(environ['QUERY_STRING'])
        data = json.dumps(app(parse))

        return [data.encode('utf-8')]

    def run():

        httpd = make_server('', 8080, application)
        print("Serving HTTP on port 8080 ...")
        httpd.serve_forever()

    if __name__ != "__main__":
        run()

