#!/usr/bin/env python3
# -*-coding:utf-8-*-
list = [1, 5, 10, 20]
a = 6
if a in list:
    print("True a is in list")
else:
    print("False")

b = 7
if a is b:
    print("a is b")
else:
    print("a not is b")


a, b = 16, 18
if a or b:
    print("a>0 and b<18")
else:
    print("error")
