#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import sys
sys.path.append("..")
from services.manager_ser import Manager
class Classes(Manager):
    def __init__(self,name,semester,course,date,classid,student,teacher,classrescord,school):
        if not isinstance(student,list):
            raise  TypeError('%s must be list' %student)
        if not isinstance(classrescord,list):
            raise TypeError('%s must be list' %classrescord)
        if not isinstance(teacher,list):
            raise TypeError('%s must be list' %teacher)
        self.name = name
        self.semester = semester
        self.course = course
        self.date = date
        self.classid = classid
        self.student = student
        self.teacher = teacher
        self.classrescord = classrescord
        self.school = school

    def add_class_record(self):
        class_record = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课次：")
