#!/usr/bin/env python3
# -*-coding:utf-8-*-
from pytpackage import file
import pytpackage
pytpackage.f1()
pytpackage.file



def f1():
    a = 2
    b = 3
    return a + b


def f2():
    print("a + b =",f1())

f2()