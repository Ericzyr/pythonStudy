#!/usr/bin/env python3
# -*-coding:utf-8-*-
try:
    t = input("input a number:")
    s = int(t)
    print(s)
except Exception as e: # ImportError,AttributeError,ValueError,
    print(e) #打印有异常结果
    print('有异常发出404')
else:
    print("没有导常结果")
finally:
    print("无论异常与否，都会执行")