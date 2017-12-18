#!/usr/bin/env python
# _*_coding:utf-8_*_

import common
def enter_out():

    inp = input("请输入url:")
    if hasattr(common, inp) == True:
        funt = getattr(common, inp)
        funt()
    else:
        print("404")

enter_out()
