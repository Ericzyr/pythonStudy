#!/usr/bin/env python
# _*_coding:utf-8_*_

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name
    #
    def talk(self):  # Abstract method, defined by convention only
        pass
    #     # print("sing")
    #     raise AttributeError('子类必须实现这个方法')
    #     # raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    # def __init__(self,name,sing):
    #     super(Cat,self).__init__(name)
    #     self.sing=sing


    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)





def func(objt):  # 一个接口，多种形态
    objt.talk()


c=Animal("t")
c1 = Cat("cat")
print(c1)
d1 = Dog("dog")

func(c1)
func(d1)
