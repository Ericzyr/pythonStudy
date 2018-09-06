#!/usr/bin/env python





def outer(fun):
    def inner():
        print('this is before')
        fun()
    return inner



@outer
def f1():
    print("this is center")



f1()



class gohome(object):
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number


class st(gohome):
    def __init__(self,name,age,number,station):
        super(st,self).__init__(name,age,number)
        self.station=station


    def cleran(self):
        print('studon go school {}'.format(self.station))

s1=st('java',23,1,'middle')
s1.cleran()
