#!/usr/bin/env python
# _*_coding:utf-8_*_
sheet = ["adf", "cd", "adsf", "t", 25, 26]
print(sheet[0:5][0:3])
sheet.insert(5, "asdf")
print(sheet)
print(sheet[0])
for i in range(len(sheet)):
    print(sheet[i])
print(type(sheet))
