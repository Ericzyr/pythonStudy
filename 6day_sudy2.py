#!/usr/bin/env python
# _*_coding:utf-8_*_


#装饰器的用法

def outer(f1):
    def inner(*args,**kwargs):
        print('this is a after')
        r = f1(*args,**kwargs)
        print('this is a befor')
        return r
    return inner


@outer
def f1(args):
    print('this is a center')
    return args

f = f1('v2')


@outer
def f2(a,b):
    print('this is a center')
    return a,b

f = f1('v2')

print(f)


f2(3, 4)
