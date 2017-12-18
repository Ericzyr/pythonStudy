#!/usr/bin/env python3
# -*-coding:utf-8-*-
from splinter.browser import Browser
import time
#b=Browser('chrome')
url='https://kyfw.12306.cn/otn/leftTicket/init'
b=Browser()
b.visit(url)