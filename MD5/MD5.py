#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib


url = "http://www.baidu.com"
url = url.encode(encoding="utf-8")

md5 = hashlib.new('md5', url).hexdigest()
print(md5)
