#!/usr/bin/env python



def outer(fun):
    def inner():
        print("before")
        fun()
        print("after")
    return inner




@outer
def f1():
    print("center")



f1()
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