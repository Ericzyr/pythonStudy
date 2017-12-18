#!/usr/bin/env python
# -*-coding:utf-8 -*-

name = "eric"

passworld = "letv123"
for i in range(10):
    if i > 2:
        break
    nameinput = input("inpunt you name:")
    #   python2.7输入函数 raw_input 和python3.5是有区别的

    passwordinput = input("input you passworld:")

    # if name == nameinput:
    #     print ("名字输入正确:")
    #     if password == passwordinput:
    #         print ("密码输入正确")
    #     else:
    #         print ("密码输入错误")
    # else:
    #     print("连名字都错误")

    if name == nameinput and passworld == passwordinput:
        print("input correct")
    else:
        print("input error......")
print("for")



