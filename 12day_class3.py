#!/usr/bin/evn python
# -*-coding:utf-8-*-
class provincial(object):


    #　静态字段
    commti = '省会之一'

    def __init__(self,name,capital,leader):
        #　动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader

    # 动态方法
    def sport_meet(self):
        print(self.Name +'正在开运动会')


    # 静态方法（加上Python自带的装饰器）
    @staticmethod
    def funt():
        print('全民运动')

    # 特性
    @property
    def bar(self):
        print(self.Name)

sd = provincial('山东','济南','王刚')

ah = provincial('安徽','合肥','张之洞')

sd.sport_meet()
print(sd.commti)

sd.funt()
sd.bar
