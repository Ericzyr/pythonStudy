#!/usr/bin/env python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
import os
import sys


ulr = r"file:///home/pc7/TV_Stress/TV_938/938cibn_1025all_tv1/20171031_1521.html"

requestcode = urllib.request.urlopen(ulr).read().decode("utf-8")

urlre =  "<td valign=\"top\" colspan=\"1\"><a href=\"(.*)\" target=\"_blank\">Click to open it</a></td>"

urlt = re.compile(urlre).findall(requestcode)

u = ".*<td><a href=\".*\" target=\"_blank\">(.*)</a></td>.*"

# u5 = re.compile(u).findall(requestcode)
# print(u5)
for i in urlt:
    print(i)















# pathcod1 = r"file://(.*)/.*.html$"
#
# pathcode = re.compile(pathcod1).findall(ulr)

# print("一共发现了", len(urlt), "个Bug")
# for i in urlt:
#     f = open(pathcode[0]+"/"+i, 'r')
#     linenumber = f.readlines()[0:3]
#     if "ANR" in linenumber[0]:
#         print("occur ANR")
#     if "FATAL EXCEPTION" in linenumber[0]:
#         print("occur FC")
#     print(linenumber[0], linenumber[1], linenumber[2])
#     f.close()
