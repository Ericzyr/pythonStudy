#!/usr/bin/env python
# _*_coding:utf-8_*_



import re
str=r"file:///home/pc7/TV_Stress/TV_938/938cibn_1025all_tv1/20171031_1521.html"

c='file:///(.*).html$'

match1=re.findall(c,str)
print(match1[0])
# result=match1.group()
# print (result)