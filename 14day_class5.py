#!/usr/bin/env python3
# -*-coding:utf-8-*-
# !/usr/bin/python
# -*- coding: UTF-8 -*-

#方法重写

class Parent(object):  # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


class A(object):
    def hello(self):
        print('Hello, i am A')
class B(A):
    pass
    # def hello1(self):
    #     print('Hello, i am B')

a = A()
b = B()
a.hello()
b.hello()
# 执行结果：
# Hello, i am A
# Hello, i am A
# 上例中可以看出class B 继承 class A 后具有了A 的方法hello()

# 下面是重写hello方法
class C(A):
    def hello(self):     # 重写hello()方法
        print('Hello, I am class C')
c = C()
c.hello()



# 执行结果：Hello, I am class C
# 当在class C 中 重新定义与父类 class A 同名的方法hellp() 后，class C 的实例将不再调用class A 中定义的hello()方法而调用
# 自身定义的hello() 方法
# 即， 子类定义父类同名函数之后，父类函数被覆盖

# 重定__init__方法
