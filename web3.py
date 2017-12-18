#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
import os
def getpage(web):
    data = urllib.request.urlopen(web).read().decode("gbk")
    return data
web = "http://quote.eastmoney.com/stocklist.html"
data = getpage(web)

def getwebcode(data):
    regex_str = "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*)\("
    getcode = re.compile(regex_str)
    codelist = getcode.findall(data)
    return codelist
codelist = getwebcode(data)


def downloadstock(code, name, date):
    path = "F:\\download\\"+date
    if not (os.path.exists(path)):
        os.makedirs(path)
    inshorsz=10
    if code[0:2]=="sh":
        inshorsz=0
    else:
        inshorsz=1
    if inshorsz !=10:
        url ="http://quotes.money.163.com/service/chddata.html?code="+str(inshorsz)+code[2:]+"&end=20170523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        path = path+"\\"+name+".csv"
        urllib.request.urlretrieve(url, path)
for i in codelist:
    downloadstock(i[0], i[1], "20170323")
