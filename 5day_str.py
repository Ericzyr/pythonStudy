#!/usr/bin/env python3
# -*-coding:utf-8-*-
# user_name = input('usrer:')
# if user_name.strip() == 'alex':     #strip()去除输入的空格
#     print('welcome')

names = 'I am good student'
m1 = names.split(' ') #对字符串分隔，按你一定方法
print(m1)

print('|'.join(m1)) #对字符串联合

print(' ' in names) #对字符有没有空格

msg = "Hello ,{n1}, it's been a long"
nam=msg.format(n1='jack') #字符串的格式化
print(nam)


age = input("your age:")
if age.isdigit():   #判断是不是数字（digit）
    age =int(age)
else:
    print('you input is type reset')