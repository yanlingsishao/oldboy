#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import pickle
import sys
sys.path.append("..")
sys.path.append("../..")
from services.manager_ser import Manager

class School(Manager):
    def __init__(self,name,address,schoolid,classes,courses):
        if not isinstance(classes,list):
            raise TypeError('%s must be list' %classes)
        if not isinstance(courses,list):
            raise TypeError('%s must be list' % courses)
        #jj = Manager().test_file_isnone("schooldb","schooldb")
        self.name=name
        self.address=address
        self.schoolid = schoolid
        self.classes = classes
        self.courses = courses

    def __iter__(self):
        return self

    def __next__(self):
        return None

    def get_classes(self):
        '''获取班级列表'''
        print("11")


