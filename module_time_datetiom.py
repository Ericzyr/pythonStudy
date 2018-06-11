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


import time

# dt = "2016-05-05 20:28:54"
#
# # 转换成时间数组
# timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# # 转换成时间戳
# timestamp = time.mktime(timeArray)
#
# print(timestamp)

# ("%.2f" % 2.565)
# >>> a

# 要求较小的2精度
#
#
# round()内置方法

# >> > round(2.5)
# 3.0
# >> > round(-2.5)
# -3.0
# >> > round(2.675)
# 3.0
# >> > round(2.675 , 2)
# 2.67