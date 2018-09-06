#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os,sys
from one import PI
import one        # start executing one.py
print("this is 4 two.py")

one.func()




if __name__ == "__main__":
    print("this is 5 two.py")
else:
    print("this is 6 two.py")



def calc_round_area(radius):
    return PI * (radius ** 2)


def main():
    print("round area: ", calc_round_area(2))

main()
