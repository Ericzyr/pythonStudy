#!/usr/bin/env python
# _*_coding:utf-8_*_


#模块time and datetiom 用法
import time
import random
import datetime

print(time.time())
print(time.ctime())
date_obj = time.localtime()
print(date_obj)
print("{year}/{month}/{day}".format(year=date_obj.tm_year, month=date_obj.tm_mon, day=date_obj.tm_mday))

tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(tm)

print(datetime.date.today())
print(datetime.datetime.now())

# 2018525_1714.html


z=time.strftime("%Y%m%d_%H%M", time.localtime())
print(z)