#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
from services.manager_ser import Manager
class Student(Manager):
    def __init__(self,name,sex,age,studentid,teacher,school,classes,course):
        if not isinstance(teacher,list):
            raise TypeError('%s must be list' %teacher)
        if not isinstance(course,list):
            raise TypeError('%s must be list' %course)
        self.studentid = studentid
        self.name = name
        self.sex = sex
        self.age = age
        self.teacher = teacher
        self.school = school
        self.classes = classes
        self.course = course

    def student_registered(self):
        student_dict = {}
        print("欢迎进入学生注册系统")
        student_name = input("注册姓名：")
        student_sex = input("性别：")
        student_school = input("学校：")
        student_class = input("班级：")
        st1 = Student(student_name, student_sex, student_school, student_class)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        self.save(self, "student", student_dict)
    def student_pay_fees(self):
        pass
    def student_view_grade(self):
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        student_name = input("姓名：")
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times \
                        and j["姓名"] == student_name:
                    for key in j:
                        print(key, j[key])
                    print("\n")
    def student_view_record(self):
        student_school = input("校名：")
        student_class = input("班级：")
        student_times = input("课次：")
        student_name = input("姓名：")
        class_record_list = Baseclass.open(self, "class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times \
                        and j["姓名"] == student_name:
                    for key in j:
                        print(key, j[key])
                    print("\n")