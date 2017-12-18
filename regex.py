#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
#!/usr/bin/python
import urllib
import urllib.request
import os
import re

ip = os.popen("ifconfig").read()
ipadres = "inet 地址:(.*)  广播:"
ipsone ="inet 地址:.*广播:.*掩码:(.*)"
getcode = re.compile(ipadres)
getcode1 = re.compile(ipsone)
codelist = getcode.findall(ip)
codelist1 = getcode1.findall(ip)
getip=codelist[0]
getip1=codelist1[0]

print("获取的电脑的IP地址：", getip)
print("获取的电脑子网掩码：", getip1)


line = "Cats are smarter than dogs"
word = re.match(r'(.*) are (.*?) .*', line)
# if word:
#         print("word.group() : ", word.group())
print("word.group(1) : ", word.group(1))
        # print("word.group(2) : ", word.group(2))
# else:
#     print("No match!!")
