#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import os,sys


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
ADMIN_DB_DIR=os.path.join(BASE_DIR,"db","admin.db")
ADMIN_AUTH_DB=os.path.join(BASE_DIR,"db","admin.json")
CLASSES_DB_DIR=os.path.join(BASE_DIR,"db","classes.db")
CLASSRECORD_DB_DIR=os.path.join(BASE_DIR,"db","classrecord.db")
COURSE_DB_DIR=os.path.join(BASE_DIR,"db","course.db")
SCHOOL_DB_DIR=os.path.join(BASE_DIR,"db","school.db")
STUDENT_DB_DIR=os.path.join(BASE_DIR,"db","student.db")
STUDYRECORD_DB_DIR=os.path.join(BASE_DIR,"db","studyrecord.db")
TEACHER_DB_DIR=os.path.join(BASE_DIR,"db","teacher.db")
print(TEACHER_DB_DIR)



