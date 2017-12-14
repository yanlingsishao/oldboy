#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
from services.manager_ser import Manager


class Courses(Manager):
    def __init__(self,name=None,courseid=None,period=None,price=None,outline=None,classes=None,school=None,teacher=None):
        if not isinstance(teacher,list):
            raise  TypeError('%s must be list' %teacher)
        self.name = name
        self.courseid = courseid
        self.period = period
        self.price = price
        self.outline = outline
        self.classes = classes
        self.school = school
        self.teacher = teacher