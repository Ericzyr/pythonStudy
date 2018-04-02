#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os
f = open('note', 'r+')
f.write("aa,")
print(f.readlines())
f.close()


os.system('ifconfig')

