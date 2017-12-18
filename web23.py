#!/usr/bin/env python3
# -*-coding:utf-8-*-


from splinter import Browser
import time


browser = Browser()
url = 'https://mail.qq.com/'
browser.visit(url)
with browser.get_iframe('login_frame')as iframe:
    iframe.find_by_id('u').fill('976207292')
    iframe.find_by_id('p').fill('z976207292')
    iframe.find_by_id('login_button').click()

