#!/usr/bin/env python
# _*_coding:utf-8_*_
def functiont(*args,**kwargs):
	print(args)
	print(kwargs)

v = {'k': 'v1', 't': 'v2'}
d = [2, 5, 4]
functiont(*d, **v)
