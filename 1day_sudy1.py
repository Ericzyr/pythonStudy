#!/usr/bin/env python
# _*_coding:utf-8_*_

# print "hello world!"
# print "你好！"
name = "jack"
# name = raw_input ("you adrress")   pyhon2.7需要加raw_input 还有一个是引用变量的时候不需要加（）
age = int(input("age:"))
# print ("name is :", name)
# print "age is :", age
# print "job is :", job

# 文本格式化
msg = '''
name: %s
age: %d
''' % (name, age)
print(msg)
print("formatting is %s" %name)