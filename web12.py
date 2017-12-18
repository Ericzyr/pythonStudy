#!/usr/bin/env python
# _*_coding:utf-8_*_
import sys
import json
# list = sys.argv
# print(list)
#
dic = {"k1": "v1"}
print(dic, type(dic))

result = json.dumps(dic)
print(result, type(result))


s2 = '{"k1":"adsf"}'
print(s2, type(s2))
dis = json.loads(s2)
print(dis, type(dis))
