#!/usr/bin/env python
# _*_coding:utf-8_*_



# 面向对象中的封装 函数在这里叫做类的 方法

class person(object):


    # 属于类时的，也叫静态字段
    comput = 'This is my desk'

    # 公共的性的属性
    def __init__(self, name, age, add):

        #动态字段
        self.Name = name
        self.Age = age
        self.Add = add

    # 功能（特有属性）
    def go_school(self,city):
        # print("%s go to school is the %s" % (self.Name,city))  #% 格式化字符串
        print("{} go to school is the {}".format(self.Name, city))   #% format 格式化字符串 两种方式
        self.city = city


    def go_work(self,where):
        print('{} work is the {}'.format(self.Name,where))






p1=person('jack',25,'shandong')   #属于对像 也叫 实例化对象


p2=person('alex',56,'beijing')

# print(p1.Name,p1.Add,p1.Age)

p1.go_school("beijing")

print(p1.city)

p2.go_work("shanghai")

