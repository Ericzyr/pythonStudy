#!/usr/bin/env python3
# -*-coding:utf-8-*-

# str 和 int 内置方法函数用法
name = "efasf"
print(dir(name))

n = name. __add__("\twoe")
print(n)



number = 0
print(dir(number))

t = number.__bool__()
print(t)


list = [2,5]
print(dir(list))

l = list.__eq__([2,3])

a = 5
print(dir(a))


a = 8
resut = a.__divmod__(5)
print(resut)

print(abs(-7))