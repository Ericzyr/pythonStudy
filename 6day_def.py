#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义函数
import os
os.system("df -h")

def addfile(filename):
    path = "/home/pc7/pythonNote/"+filename
    # 判断一个文件是不是存在
    if (os.path.exists(path)) is False:
        os.mkdir(path)

inputfile= input("输入文件名字：")
addfile(inputfile)

path1 = "/home/pc7/pythonNote/"
dir = os.listdir(path1)
print(dir)
print(os.name)