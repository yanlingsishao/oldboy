#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import sys
sys.path.append("..")
sys.path.append("../..")
from services.manager_ser import Manager


class Teacher(Manager):
    def __init__(self,name,age,sex,assets,id,student,school,classes,course):
        if not isinstance(student,list):
            raise TypeError('%s must be list' %student)
        if not isinstance(classes,list):
            raise TypeError('%s must be list' %classes)
        if not isinstance(course,list):
            raise TypeError('%s must be list' %course)
        self.name=name
        self.age=age
        self.sex=sex
        self.__assets = assets
        self.id=id
        self.student=student
        self.school = school
        self.classes = classes
        self.course = course

    def add_class_record(self):
        class_record = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课次：")


    def corrects_stus_papers(self):
        '''批改学生作业'''
        pass

    def oo(self):
        print("nima")