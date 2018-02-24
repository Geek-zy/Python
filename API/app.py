#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# API 调用实例
# http://127.0.0.1:8080/?name=Geek&user=root

from api import api


@api
def app(parse):

    name = parse.get('name', [''])[0]
    user = parse.get('user', [''])[0]

    data = {'name': name, 'user': user}

    return data

