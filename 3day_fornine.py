#!/usr/bin/env python
# _*_coding:utf-8_*_
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print(j, "*", i, "=", i*j, " ",  end="")
    print("")




