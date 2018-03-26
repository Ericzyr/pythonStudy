#!/usr/bin/env python
# _*_coding:utf-8_*_


# list_number = [25, 26, 77, 88, "hello"]
# for i in list_number:
#     print(i)




# list sheet study

sheet = ["adf", "cd", "adsf", "t", 25, 26, 9, 99, 68]

print(sheet)


print(sheet[0])  # 切片
print(sheet[0:5][0:3])  # 切片

sheet[1] = 'wwww'  #修改

sheet.append("po")  # 从后附加(append)一个

sheet.insert(5, "asdft")  # 从下标第几个 插入(insert)

sheet.remove("t")   # 移除(remover)数据

del sheet[3:5]  # 删除下标的任意一个数据
print(sheet)

print(sheet[::2]) #步长

if 9 in sheet: # 判断一个数是否在列表中
    number = sheet.count(9) #求一个数的个数是多
    number_index = sheet.index(68) #求一个数的下标是多少
    print(number_index)
print(list)
print(number)
print('9 is in sheet', number)


# for i in range(len(sheet)):
#     print(sheet[i])
# print(type(sheet))

name1 = [25, 1, 2, 4, 6]
name2 = [69, 28]
name1.extend(name2) #列表的合并
name1.sort() #列表的排列（只针对相同的数据列表的）
name1.pop(0) #删除一个数据的索引数据
name3=name2.copy() #列表的copy

print(name1)



# 对列表的去重
list = [2,4,2,5,6,5,6,]
new_list = []
for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

list.sort() #排序
list.reverse()#反排序





