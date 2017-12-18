#!/usr/bin/env python3
# -*-coding:utf-8-*-
import re
import urllib
import urllib.request
urlt = 'http://daily.zhihu.com'
def gethtml(urlt):
    headerst = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'}
    request = urllib.request.Request(urlt, headers=headerst)
    getu = urllib.request.urlopen(request).read().decode("utf-8")
    return getu

gethtml(urlt)

def geturl():
    patten = re.compile('<a href="/story/(.*?)"', re.S).findall(gethtml(urlt))
    # print(patten)
    return patten
listt =[]
for i in geturl():
    listt.append("http://daily.zhihu.com/story/"+i)

for t in listt:
    print(t)