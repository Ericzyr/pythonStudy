#!/usr/bin/env python
# _*_coding:utf-8_*_

import reflect_common


#反射 getattr 从导入函数中查找字符串，并获取
#反射 hasattr 从导入函数中查找字符串，如果有的话返回True 没有的话返回false

def enter_out():
    inp = input("请输入url:")
    if hasattr(reflect_common, inp) == True:
        funt = getattr(reflect_common, inp)
        funt()
    else:
        print('404')
enter_out()
