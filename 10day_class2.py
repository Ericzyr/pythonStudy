#!/usr/bin/env python3
# -*-coding:utf-8-*-


# 面向对象中的继承

class school_member(object):


    number = 0

    def __init__(self,name, age, sex):
        self.Name = name
        self.Age = age
        self.Sex = sex
        self.enroll()


    def enroll(self):
        print('sort {0} this {1} go school'.format(school_member.number,self.Name))
        school_member.number += 1


# 面向对象中的继承school_member
class teachers(school_member):
    def __init__(self,name, age, sex,course,salary):  #先把对象继承过来，再格式化
        super(teachers,self).__init__(name,age,sex)
        self.Course = course
        self.Salary = salary

    def teach_lesson(self):
        print('{0} teach is lesson'.format(self.Name))



# 面向对象中的继承school_member
class student(school_member):
    def __init__(self,name, age, sex,course,puy):   #先把对象继承过来，再格式化
        super(student,self).__init__(name, age, sex)
        self.Course = course
        self.Puy = puy

    def student_leran(self,lesso):
        print('{0} learing is course {1}'.format(self.Name,lesso))


t1 = teachers('Jack','25', 'F', 'Python', '2000')

t2 = teachers('Tome','24', 'X', 'Linux', '2500')


s1 = student('student_alxs','22', 'S', 'Jave', '1500')

s2 = student('student_april','23', 'L', 'Shell', '1400')


t1.teach_lesson()
s1.student_leran("python")
