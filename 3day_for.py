#!/usr/bin/env python
# -*-coding:utf-8 -*-


for i in range(10):
    name, passworld = "eric", "letv123"
    ninput, pinput = input("inpunt you name:"), input("input you passworld:")
    if i > 2:
        break
    if name == ninput and passworld == pinput:
        print("输入正确")
        break
    else:
        print("输入错误")
    print("asdf")
