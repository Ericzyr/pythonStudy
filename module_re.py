#!/usr/bin/evn python
# -*-coding:utf-8-*-

#python 正则表达式　

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
print(sp)
