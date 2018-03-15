#!/usr/bin/env python
# _*_coding:utf-8_*_

import os
print("hello world")
print("你好！")

print(os.getcwd())  #获取当前路径

print(os.popen("df -h").read())   #获取当前电脑的内存

print(os.popen("ifconfig enp4s0|grep inet").read())  #获取当前电脑的IP地址




name = "eric"

age = 25

print(name, age)
