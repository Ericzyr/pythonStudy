#!/usr/bin/env python3
# -*-coding:utf-8-*-

import urllib.request
url = 'http://bj.meituan.com/'


req = urllib.request.urlopen(url).read().decode("utf-8")

print(req)