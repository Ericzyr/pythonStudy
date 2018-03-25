#!/usr/bin/env python3
# _*_coding:utf-8_*_
#字符串转换成字符类型

# s = "我的朋友"
#
# n = bytes(s, encoding="utf-8")
#
# print(n)
#
# n1 = bytes(s, encoding="gbk")
#
# print(n1)


r = input("pleas you input a number:")
def fun(*agrs):
    if agrs == '12':
        z = open('note', 'r', encoding='utf-8').readlines()
        for i in range(len(z)):
            print(z[i])
        else:
            print('no')
fun(r)