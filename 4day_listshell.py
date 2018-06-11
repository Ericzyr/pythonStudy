#!/usr/bin/env python
# _*_coding:utf-8_*
import sys
import os

sheet = ["adf", "cd", "adsf", "t", 25, 26]


print(sheet[0:5][0:3])
sheet.insert(5, "asdf")
print(sheet)
print(sheet[0]+'\n')



for i in range(len(sheet)):
    print(sheet[i])
print(type(sheet))



a=[[1,2],[3,4]]

print(tuple(a))

print(a[1][0],type(a))

#path = "F:\\download\\"+date
path1 = '/home/pc7/pythonStudy/web11.py'

if os.path.exists(path1):
    print("true")
else:
    print('false')
