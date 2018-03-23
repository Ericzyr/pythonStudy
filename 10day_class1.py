#!/usr/bin/env python3
# -*-coding:utf-8-*-
class person:

    comput = 'This is my desk' #属于类时的，也叫静态字段
    def __init__(self,name,age,add):
        #动态字段
        self.Name = name
        self.Age = age
        self.Add = add

p1=person('jack',25,'shandong')   #属于对像 也叫
p2=person('alex',56,'beijing')





print(p1.Name,p1.Add,p1.Age)