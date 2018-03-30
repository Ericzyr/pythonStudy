#!/usr/bin/env python3
# -*-coding:utf-8-*-

class person(object):
    def __init__(self,name,age,sex,add,phone):
        self.Name = name
        self.Age = age
        self.Add = add
        self.Sex = sex
        self.Phone = phone

    def work_department(self,department):
        print('{}工作部门是{}'.format(self.Name,department))


class MTBF_group(person):
    def __init__(self,name,age,sex,add,phone,duty,doing):

        super(MTBF_group,self).__init__(name,age,sex,add,phone)
        self.Duty = duty
        self.Doing = doing

    def auto_MTBF(self,write):
        print('{}{}做的工作是{}'.format(self.Name,self.Duty,write))


class Stress_group(person):
    def __init__(self,name,age,sex,add,phone,auto,duty):
        super(Stress_group,self).__init__(name,age,sex,add,phone)
        self.auto = auto
        self.Duty = duty

    def auto_Stress(self,write):
        return write
        print('{}'.format(write))




p1 = MTBF_group('张三','25','男','北京','13510252168',"自动化组",'MTBF测试')
p2 = Stress_group('黄雷','24','女','天津','1358410088','手动组','手动测试')