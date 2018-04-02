#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
#!/usr/bin/python
import urllib
import urllib.request
import os
import re


ipadres,ipsone = "inet 地址:(.*)  广播:","inet 地址:.*广播:.*掩码:(.*)"
# ipsone ="inet 地址:.*广播:.*掩码:(.*)"

def ip_functiom(args):
    ip = os.popen("ifconfig").read()
    getcode = re.compile(args)
    codelist = getcode.findall(ip)
    getip = codelist[0]
    if  args == ipadres:
        print("获取的电脑的IP地址：", getip)
    elif args == ipsone:
        print("获取的电脑子网掩码：", getip)
    else:
        print('4040')



ip_functiom(ipadres)

ip_functiom(ipsone)









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
