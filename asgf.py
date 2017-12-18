#!/usr/bin/env python
import re
import urllib

# f = open("/home/pc7/TV_Stress/TV_938/938_all0803/938TV3/LOOP1/testDesktop_20170803_183358/logstack.log", "r")
# t=(f.read())
# print(t)

# filehtml ="file:///home/pc7/TV_Stress/TV_938/938_all0803/adsf/afabg/2017asdf18_1616.html"
#
# fi = "file://(.*)/.*.html$"
# urlt = re.compile(fi).findall(filehtml)
# print(urlt[0]+"/")

# theList = ["ar", "bc", "cc"]
# if "a" in theList:
#     print("a inthelist")
#
# if "d" not in theList:
#     print ("d is notinthelist")

site = 'http://www.jb51.net/'
if "jb51" in site:
   print('site contains jb51')