#!/usr/bin/env python
# _*_coding:utf-8_*_

#火车票爬虫
import urllib
import urllib.request
import json
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context  #有证书请求需要加入
def getlist():
    req = urllib.request.urlopen("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-30&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT")
    html = req.read().decode("utf-8")
    u = json.loads(html)
    return u['data']['result']
for i in getlist():
    print(re.sub(r'^.*订|', "", i))



