#!/usr/bin/evn python
# -*-coding:utf-8-*-

#python 正则表达式　
import os
import re

str = 'This is my1 desk'
s = re.findall('^T.*k$', str)#搜索查找

""" 

^表示以什么开始　$表示以什么结束　.表示任意一个字符　*表示多个字符　+表示１至多个字符

"""

print(s)

# m = re.match('is',str).group() #从头搜索
m = re.search('This',str).group()# 匹配搜索
print(m)
#
# z = re.sub("is",'have',str,1)     #替换
# z = re.subn("is",'have',str,1)　　#替换
# print(z)

sp = re.split(' ',str) #分割
print(sp,'\n')



ip = os.popen('ifconfig').read()



get = re.compile('inet 地址:(.*)广播:').findall(ip)

print("电脑的IP地址：",get[0],'\n')

def f1():
    df = os.popen('df -h').read()
    print(df,'\n')

    df_file = re.compile('/dev/sda1(.*)%').findall(df)
    print(df_file[0])
f1()

