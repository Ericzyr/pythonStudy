#!/usr/bin/env python3
# -*-coding:utf-8-*-
import json
#
def outfuntion(function):
    def innerfuntion(*args,**kwargs):
        print("A")
        function(*args,**kwargs)
    return innerfuntion





@outfuntion
def f1(*args,**kwargs):
    print("hello world",*args,**kwargs)


st = [1,2]
set = {'name':'jack','age':25}
f1(*st,set)


print('\t')

@outfuntion
def f2():
    print("two")
f2()