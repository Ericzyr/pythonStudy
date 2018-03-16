#!/usr/bin/env python3
# -*-coding:utf-8-*-

# 传参和万能参数 函数
def functiont(*args, **kwargs):
    print(args)
    print(kwargs)


v = {"k": 123, "t": 456}

d = [2, 5, 4, "wq"]

functiont(*d, **v)

print(type(v), type(d))  # get list and dict 属性