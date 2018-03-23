#!/usr/env/bin python
#-*-coding:utf-8-*-

# list = [2,3,5,8]
# for i in range(len(list)):
#     print(list[i])


# 生成器  必须有 yield 出现

def function():
    print('you is girl')
    yield 'girl'
    print('I am boy')
    yield 'boy'

for item in function():
    print(item)