#!/usr/bin/env python
# _*_coding:utf-8_*_
import re
import urllib
import urllib.request
import os

web = "http://bbs.zol.com.cn/dcbbs/gallery_d657_45698.html#p7"
getweb = urllib.request.urlopen(web).read().decode("gbk")

webre ="<li class=\"on\"><img src=\"(.*)\" alt=\"(.*?)\"/></li>"

getcode = re.compile(webre).findall(getweb)

def download(urlcode, name):
    url = urlcode
    path = "/home/pc7/myfile/download/"+name+".jpg"
    urllib.request.urlretrieve(url, path)

for code in range(len(getcode)):
    sub1 = (getcode[code][0])
    strinfo = re.compile('100x75c4')
    sub2 = strinfo.sub('1200x5000', sub1)
    download(sub2, getcode[code][1]+str(code))

print(os.getcwd())
