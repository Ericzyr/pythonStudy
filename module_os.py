#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os

import sys

t = os.getcwd()

os.chdir('/home/pc7/pythonNote')
#os.rmdir('web99.py')


print(t)


for i in os.listdir(t):
    print(i)



v = sys.argv[0]   #在启用时候要传python.py 外传一个参数 0是第一个参数  1是第二个参数
print(v)