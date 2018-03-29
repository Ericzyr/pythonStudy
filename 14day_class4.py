#!/usr/bin/env python3
# -*-coding:utf-8-*-


# python之类方法的重载 类中的重载方法str

class Vector(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print("str 重载方法")
        return 'ok'
        #return 'Vector (%d, %d)' % (self.a, self.b)
        #return 'Vector{} {}'.format(self.a, self.b)

    # def __add__(self, other):
    #     return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)


print(v1)




# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)