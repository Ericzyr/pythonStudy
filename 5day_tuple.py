#!/usr/bin/env python3
# -*-coding:utf-8-*-


#元组学习tuple 元组不能修改，（元素值），可以合并元组

t1 = (25, 26, 28)
print(t1, type(t1))

t2 = ('a', 'b', 'c', 'd')

list = ['sa','ac','d','ps']


print(t2[0:2]) #元组的访问

t3 = t1 + t2  #元组的合并

print(t3)


t4 = tuple(list)  #列表可以转化为元组
print(t4)


'''
元组 

del tuple  删除元组
len(tuple) 计算元组元素的个数
max(tuple) 返回元组的最大值
min(tuple) 返回元组的最小值
tuple(seq) 列表转化为元组

'''

