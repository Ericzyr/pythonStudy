#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
def download():
    url = "http://b.hiphotos.baidu.com/image/h%3D300/sign=0a17f707f5039245beb5e70fb796a4a8/b8014a90f603738d60ae0de8ba1bb051f919ec10.jpg"
    path = "F:\\download\\1.jpg"
    urllib.request.urlretrieve(url, path)
download()
