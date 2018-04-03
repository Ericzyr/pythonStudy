#!/usr/bin/evn python
# -*-coding:utf-8-*-
import os
import re


ip = input("please input TV's IP address:")
ip_add = os.popen('adb connect '+ip).read()
ip_devices = os.popen('adb devices').read()

if  ip_add[0:7] == 'already':
    print('connect sucess')
elif ip_add[0:6] == 'unable':
    print('unconnect faile')


print(ip_add[0:7])
print(ip_devices)