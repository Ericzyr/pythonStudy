# !/usr/bin/python


#  字典的学习
dict = {"001": {"name": "jack", "age": 25, "add": "beijing"}, "002": {"name": "adfack", "age": 21, "add": "beijing"}}
dict["001"]["name"] = "bill"
print(dict["001"])




d = {"a":5,"b":6}
print(d)



dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

#字典的访问
print ('Name:', dict1['Name'])
print ('Age:', dict1['Age'])


print(str(dict1)) #	str(dict) 输出字典，以可打印的字符串表示。

print(type(dict1))


#打印出字典的所有用法
print(dir(dict1))
'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
'''
