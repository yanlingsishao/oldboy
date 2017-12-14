#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''

from services.manager_ser import Manager
class ClassRecord(Manager):
    '''上课记录'''
    def __init__(self,name,classes,teacher,section,coursedate,studyrecord,id):
        if not isinstance(studyrecord,list):
            raise TypeError('%s must be list' %studyrecord)
        self.name = name
        self.classes = classes
        self.teacher = teacher
        self.section = section
        self.coursedate = coursedate
        self.studyrecord = studyrecord
        self.id = id