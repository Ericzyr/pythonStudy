#!/usr/bin/env python3
# -*-coding:utf-8-*-



#
# def outer(fun):
#     def inner(*args,**kwargs):
#         print('before')
#         ret=fun(*args,**kwargs)
#         print('after')
#         return ret
#     return inner
#
#
#
#
# @outer
# def f1(*args,**kwargs):
#     print(args,kwargs)
#     return 'ok'
#
#
#
#
# return_value=f1(2,5,[2,5],{'k':5,'k2':6},k=25)
# print(return_value)


#继承
# class student(object):
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age =age
#         self.address =address
#
#     def f1(self):
#         print('{}go to school'.format(self.name))
#
# s = student('jack',12,'北京')
# s.f1()
#
#
# class school(student):
#     def __init__(self,name,age,address,photo):
#         super(school,self).__init__(name,age,address)
#         self.photo=photo
#
#     def who(self):
#         print('{} tell give me {}'.format(self.name,self.photo))
#
#
# s1=school('jack',12,'北京',123)
#
# s1.who()




#生成器和迭代器
# def fun():
#
#     yield 'gekk'
#
#     yield 2
#
# ret=fun()
#
# f1=ret.__next__()
#
#
# f2=ret.__next__()
#
#
#
# print(f2)
# print(f1)





class persion(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def learn(self):
        print("{} learning Enlish".format(self.name))

class pre(object):
    def __init__(self):
        pass
    def eat(self):
        print("you eating meat")


class student(persion,pre):
    def __init__(self,name,age,nubmer):
        super(student,self).__init__(name,age)
        self.number=nubmer



s2=persion("jack",23)
s1=student("tom",19,"middle scholl")
s1.learn()
s1.eat()












































































































