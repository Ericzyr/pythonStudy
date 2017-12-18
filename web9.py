#!/usr/bin/env python
# _*_coding:utf-8_*_

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name =name
        self.age =age
        self.sex = sex


    def enroll(self,name):
        self.name=name
        print("SchoolMember[%s]is enrooled!" %self.name)


studen = SchoolMember("af",25,"s")

t=studen.enroll("jack")
