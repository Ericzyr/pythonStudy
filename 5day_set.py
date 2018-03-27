# !/usr/bin/python
# _*_coding:utf-8_*_
# dic ={"物品": "电脑"}
#
# print(dic["物品"])
#
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# print(dict['Name'])
# print(dict['Age'])
# print(type(dict))

#  集合的学习 特点不可以通加下标查找元素值

settv = {12, 13, 34, 12, 6, 5, "tev"}


settv.add("pcand")  # 增加
settv.discard(12)  # 移除
settv.remove(13)  # 移除
t = settv.pop()  # 随机除一个

print(t)

print(settv)
print(type(settv))
