#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os

t = os.getcwd()

os.chdir('/home/pc7/pythonNote')
#os.rmdir('web99.py')


print(t)


for i in os.listdir(t):
    print(i)

