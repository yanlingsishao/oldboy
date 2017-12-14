#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年9月11日
@author: WangQiyuan

'''

import pickle
import hashlib
import time
import os,sys
import pexpect

class Manager:
    def create_md5(self):
        m = hashlib.md5()
        m.update(str(time.time()).encode('utf-8'))
        return m.hexdigest()

    def test_file_isnone(self,dir,file):
        '''测试文件是否为空'''
        name = self.get_name(dir,file)
        return name

    def get_name(self,dir,file):
        if os.path.isdir(dir) == False:
            os.mkdir(dir)
        if os.path.isfile('{}\{}.db'.format(dir,file)) == False:
            if sys.platform in ["win32","windows"]:
                os.system("type nul > {}\{}.db".format(dir,file))
                return []
        else:
            with open('{}\{}.db'.format(dir,file),'rb') as f:
                try:
                    files = pickle.load(f)
                    return files
                except EOFError as e:
                    return []

    def save(self,dir,file,obj):
        isnonefile = self.get_name(dir, file)
        isnonefile.append(obj)
        with open('{}\{}.db'.format(dir,file),'wb') as f:
            pickle.dump(isnonefile,f)

    def save_db(self,dir,file,obj,all_obj_list):
        #isnonefile = self.get_name(dir, file)#所有数据
        index_value = all_obj_list.index(obj)
        all_obj_list[index_value]=obj
        with open('{}\{}.db'.format(dir,file),'wb') as f:
            pickle.dump(all_obj_list,f)

    def set_db(self,dir,file,onlyidname,onlyidvalue):
        default_modify_list = []#设置onlyidname列表
        default_id_list = []#设置onlyidvalue对象列表
        dict_obj = Manager().get_name(dir,file)#查找原始所有数据，是个列表
        for i in dict_obj:
            if i.__dict__.get(onlyidname) == onlyidvalue:
                default_modify_list.append(onlyidvalue)#添加
                default_id_list.append(i)

            '''对象字典
            dic_obj:所有原始数据
            default_modify_list：唯一id的列表
            i:唯一id的对象'''
        return (dict_obj,default_modify_list,default_id_list)

    def add_db(self,dir,file,modify_name,add_name,onlyidname,onlyidvalue):
        '''列表增加数据
        modify_name   对象拥有可以扩展列表的方法名
        change_name   需要增加的对象中的表值
        modify_value
        'teacher'，可添加student
        'school' 可添加classes,courses
        'student' 可添加teacher
        'class' 可添加student,teacher,classrescord
        'course' 可添加classes'''
        need_change = self.set_db(dir,file,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]#
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value = all_obj_list.index(i)
            i.__dict__[modify_name].append(add_name)
            i.save_db(dir,file,i,all_obj_list)

    def del_db(self,dir,file,modify_name,del_name,onlyidname,onlyidvalue):
        need_change = self.set_db(dir,file,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value_list = i.__dict__[modify_name]
            if index_value_list.count(del_name) != 0:
                del_index = index_value_list.index(del_name)
                index_value_list.pop(del_index)
                i.save_db(dir,file,i,all_obj_list)
            return None

    def change_db(self,dir,file,modify_name,before_change,after_change,onlyidname,onlyidvalue):
        need_change = self.set_db(dir,file,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value_list = i.__dict__[modify_name]
            if type(index_value_list) == list:
                if index_value_list.count(before_change) != 0:
                    before_change_index = index_value_list.index(before_change)
                    index_value_list[before_change_index] = after_change
                    i.save_db(dir,file,i,all_obj_list)
                return None
            else:
                i.__dict__[modify_name] = after_change
                i.save_db(dir,file,i,all_obj_list)

    def find_db(self,dir,file,modify_name):
        '''dir:目录名
           file:文件名
           modify_name:'''

    def del_obj(self,dir,file,delname):
        course_obj_list = self.get_name(dir,file)
        for i in course_obj_list:
            if i.name == delname:
                l = course_obj_list.index(i)
                course_obj_list.pop(l)
            else:
                continue
        print(course_obj_list)
        os.system("type nul > {}\{}.db".format(dir, file))
        for k in course_obj_list:
                k.save(dir,file,k)

    def add_teacher(self,student):
        '''添加老师'''
        name=input("请输入老师姓名:")
        sex=input("请输入老师性别:")
        age=input("请输入老师年龄:")
        assets=input("请输入老师资产")
        teacherid = Manager().create_md5()
        teacher_obj = Teacher(name,age,sex,assets,teacherid,student)
        teacher_obj.save("teacherdb","teacherdb",teacher_obj)
        return self

    def add_school(self,classes,courses):
        name = input("请输入学校名:")
        addr = input("请输入学校地址:")
        schoolid = Manager().create_md5()
        school_obj = School(name,addr,schoolid,classes,courses)
        school_obj.save("schooldb","schooldb",school_obj)
        return self

    def add_student(self,teacher):
        name = input("请输入学生姓名:")
        sex = input("请输入学生性别:")
        age = input("请输入学生年龄:")
        studentid = Manager().create_md5()
        student_obj = Student(name,sex,age,studentid,teacher)
        student_obj.save("studentdb","studentdb",student_obj)
        return self

    def add_the_class(self,student,teacher,classrescord):
        '''创建班级'''
        name = input("请输入班级名:")
        semester = input("请输入学期:")
        course = input("请输入课程:")
        date = input("请输入开课日期:")
        classid = Manager().create_md5()
        the_class = Classes(name,semester,course,date,classid,student,teacher,classrescord)
        the_class.save("classesdb","classesdb",the_class)
        return self

    def add_course(self,classes):
        name = input("请输入课程名:")
        period = input("请输入学期:")
        price = input("请输入价格:")
        outline = input("请输入大纲:")
        course = Courses(name,period,price,outline,classes)
        course.save("coursedb","coursedb",course)
        return self


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

    def get_courses(self):
        for k in Manager().get_name("schooldb","schooldb"):
            print(k.__dict__)

    def get_classes(self):
        '''获取班级列表'''
        print("11")



class Courses(Manager):
    def __init__(self,name,period,price,outline,classes):
        self.name = name
        self.period = period
        self.price = price
        self.outline = outline
        self.classes = classes


class Classes(Manager):
    def __init__(self,name,semester,course,date,classid,student,teacher,classrescord):
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


class Teacher(Manager):
    def __init__(self,name,age,sex,assets,id,student):
        if not isinstance(student,list):
            raise TypeError('%s must be list' %student)
        self.name=name
        self.age=age
        self.sex=sex
        self.__assets = assets
        self.id=id
        self.student=student

    def add_class_record(self):
        pass

    def corrects_stus_papers(self):
        '''批改学生作业'''
        pass

    def oo(self):
        print("nima")


class ClassRecord(Manager):
    '''上课记录'''
    def __init__(self,teacher,classes,section,coursedate):
        self.teacher = teacher
        self.classes = classes
        self.section = section
        self.coursedate = coursedate
        self.lala = {classes:[teacher,section,coursedate]}




class StudyRecord(Manager):
    def __init__(self,sigh_status,sigh_date,student,achievement,section):
        if section not in self.get_name():
            self.lala = {section: {sigh_date: [sigh_status, student, achievement]}}

        self.sigh_status = sigh_status
        self.sigh_date = sigh_date
        self.achievement = achievement
        self.classrecord = classrecord


class Student(Manager):
    def __init__(self,name,sex,age,studentid,teacher):
        if not isinstance(teacher,list):
            raise TypeError('%s must be list' %teacher)
        self.studentid = studentid
        self.name = name
        self.sex = sex
        self.age = age
        self.teacher = teacher

    def optional_courses(self):
        '''自选课程'''
        pass

    def go_to_class(self):
        '''上课'''
        pass

    def see_courses(self):
        '''查看已选课程'''
        pass

    def see_class_record(self):
        '''查看上课记录'''
        pass

    def appraise_teacher(self):
        '''评价老师'''
        pass

def dict_db():
    dict_dbs={1:["schooldb","学校"],
              2:["teacherdb","教师"],
              3:["studentdb","学生"],
              4:["coursedb","课程"],
              5:["classesdb","班级"],
              6:["classrecorddb","上课记录"],
              7:["studyrecorddb","学习记录"]}
    while True:
        print("id  name")
        for i in dict_dbs.keys():
            print("{}  {}".format(i,dict_dbs[i][1]))
        z = int(input("请输入需要查询的id:"))
        for k in Manager().get_name(dict_dbs[z][0],dict_dbs[z][0]):
            print(k.__dict__)
        return None

if __name__ == "__main__":
    # for i in Manager().get_name("coursedb","coursedb"):
    #     print(i.__dict__)
    #Manager().add_course("23")
    #Manager().del_obj("coursedb","coursedb","1")
    #count = 0
    # for i in Manager().get_name("schooldb","schooldb"):
    #     i.get_classes()
    dict_db()


    #o = Manager().add_teacher(["liuren"])
    #o = Manager().add_db("schooldb","schooldb","classes","2")
    #x = Manager().add_db("schooldb","schooldb","courses","linux","schoolid","ecac7ea415e2a8f30dcc52c3bd75832e")
    #print(x)

    #o = Manager().add_the_class(["niubi"],["niubi"],["cdfasd"])

    # t1 = School("wangq", "ff", "fda",["fdas"],["fasd"])