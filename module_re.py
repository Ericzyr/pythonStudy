#!/usr/bin/evn python
# -*-coding:utf-8-*-

#python 正则表达式　
import os
import re

str = 'This is my1 desk'
s = re.findall('^T.*k$', str)#搜索查找

''' 

^表示以什么开始　$表示以什么结束　.表示任意一个字符　*表示多个字符　+表示１至多个字符



re.match与re.search的区别

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。




compile(编译、编制) 函数

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：
re.compile(pattern[, flags])




findall（全文查找）

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

语法格式为：

findall(string[, pos[, endpos]])

'''

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
    df_file = re.compile('/dev/sda(.*)%').findall(df)
    print(df_file)

    s = df_file[0]

    q=s.replace(" ","")


    print('查看电脑存贮量剩余：',q[-2:])
f1()

