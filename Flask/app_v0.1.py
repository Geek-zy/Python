#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# 使用 route 定义路由规则
@app.route('/')
def index():
    return '<h1>Hello Word!</h1>'

@app.route('/<name>')
def user(name):
    return '<h1>Hello %s' % name

if __name__ == "__main__":
    app.run()
