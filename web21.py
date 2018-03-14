#!/usr/bin/env python3
# -*-coding:utf-8-*-
# coding=utf-8
import time
from splinter import Browser


def splinter(url):
    browser = Browser()
    browser.visit(url)
    time.sleep(2)
    browser.find_by_id('login-form-username').fill('ext-yuren.zhang')
    browser.find_by_id('login-form-password').fill('@##456789t')
    browser.find_by_id('login').click()
    time.sleep(8)
    # # close the window of brower
    # browser.quit()


if __name__ == '__main__':
    websize3 = 'http://jira.letv.cn/secure/Dashboard.jspa'
    splinter(websize3)
