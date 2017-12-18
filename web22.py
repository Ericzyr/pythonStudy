#!/usr/bin/env python3
# -*-coding:utf-8-*-
from splinter import Browser
import time


browser = Browser()
url = "http://mail.163.com/"
browser.visit(url)
time.sleep(2)
with browser.get_iframe('x-URS-iframe')as iframe:
    iframe.find_by_name('email').fill('zyrarter')
    iframe.find_by_name('password').fill('zyr519328')
    iframe.find_by_id('dologin').click()




