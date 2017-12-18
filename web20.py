#!/usr/bin/env python3
# -*-coding:utf-8-*-


#
# from splinter import Browser
# browser = Browser()
import time

from splinter import Browser
browser = Browser()
url = "http://www.baidu.com"
browser.visit(url)
# browser.fill('wd', 'English study')
browser.find_by_name('wd').fill('163邮箱登陆')
browser.find_by_id("su").click()
time.sleep(2)

browser.driver.switch_to_window(browser[-1])