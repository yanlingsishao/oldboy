#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import pickle
import hashlib
import time
import os,sys
from prettytable import PrettyTable

sys.path.append("..")
sys.path.append("../..")
from services.course_ser import Courses
from services.manager_ser import Manager
from services.school_ser import School
from services.teacher_ser import Teacher
from services.class_ser import Classes
from services.classrecord_ser import ClassRecord
from services.student_ser import Student
from services.studyrecord_ser import StudyRecord
from conf import settings



class Admin_ser(Manager):
    "admin类"
    dict_all_value = {1: ["学校", settings.SCHOOL_DB_DIR,
                          ["name", "classes", "courses", "address", "schoolid"],
                          ["classes", "course"],  # 可添加的名字
                          ["name", "address"],
                          "Admin_ser().add_school"],  # 可修改的名字
                      2: ["课程", settings.COURSE_DB_DIR,
                          ["name", "period", "price", "outline", "classes", "school","courseid"],
                          ["classes"],
                          ["name", "period", "price", "outline","school"],
                          "Admin_ser().add_course"],
                      3: ["班级", settings.CLASSES_DB_DIR,
                          ["name", "semester", "course", "date","school", "student", "teacher", "classrescord", "classid"],
                          ["student", "teacher", "classrescord"],
                          ["name", "semester", "course"],
                          "Admin_ser().add_the_class"],
                      4: ["学生", settings.STUDENT_DB_DIR,
                          ["name", "sex", "age", "teacher","school","classes","course", "studentid"],
                          ["teacher","course"],
                          ["name", "sex", "age","school","classes",],
                          "Admin_ser().add_student"],
                      5: ["老师", settings.TEACHER_DB_DIR,
                          ["name", "age", "sex", "student","school","classes","course", "id"],
                          ["student","classes","course"],
                          ["name", "age", "sex","school"],
                          "Admin_ser().add_teacher"],
                      6: ["上课记录", settings.CLASSRECORD_DB_DIR,
                          ["name", "classes", "teacher", "section", "coursedate", "studyrecord", "id"],
                          ["studyrecord",],  # 可添加的名字
                          ["name", "classes", "teacher", "section","coursedate",],
                          "Admin_ser().add_classrecord"],
                      7: ["学习记录", settings.STUDYRECORD_DB_DIR,
                          ["name","sigh_status","sigh_date","student","achievement","section","id"],
                          ["classes", "course"],  # 可添加的名字
                          ["sigh_status",],
                          "Admin_ser().add_studyrecord",
                          ["achievement"]],
                      8: ["返回上一页"]}

    def ret(self):
        return 0

    def interactive(self,menu, menu_dict):
        exit_flag = False
        while exit_flag != "b":  # 不为b，则一直循环
            print(menu)
            user_option = input(">>:").strip()
            if user_option in menu_dict.keys():
                # print(menu_dict[user_option])
                exit_flag = eval(menu_dict[user_option])
                return exit_flag
            else:
                print("\033[31;1mOption does not exist!\033[0m")

    def grep_obj(self,dir, find_name):
        '''当名字为find_name时，获取各人员的对象，返回0：对象的地址，返回1：对象的字典值'''
        x = self.get_allobj_list(dir)
        if x != None:
            for (key, value) in x.items():
                if value["name"] == find_name:
                    return key, value
        else:
            return None, x

    def grep_db(self,dir,onlyidname,onlyidvalue):
        "返回对应的字典"
        all_obj_dic = self.get_allobj_list(dir)
        if all_obj_dic:
            for key,value_dic in all_obj_dic.items():
                if value_dic[onlyidname] == onlyidvalue:
                    return value_dic

    def set_db(self,dir,onlyidname,onlyidvalue):
        default_modify_list = []#设置onlyidname列表
        default_id_list = []#设置onlyidvalue对象列表
        dict_obj = Manager().get_name(dir)#查找原始所有数据，是个列表
        for i in dict_obj:
            if i == None:
                continue
            if i.__dict__.get(onlyidname) == onlyidvalue:
                default_modify_list.append(onlyidvalue)#添加
                default_id_list.append(i)
            '''对象字典
            dic_obj:所有原始数据
            default_modify_list：唯一id的列表
            i:唯一id的对象'''
        return (dict_obj,default_modify_list,default_id_list)

    def add_db(self,dir,modify_name,add_name,onlyidname,onlyidvalue):
        '''列表增加数据
        modify_name   对象拥有可以扩展列表的方法名
        change_name   需要增加的对象中的表值
        modify_value
        'teacher'，可添加student
        'school' 可添加classes,courses
        'student' 可添加teacher
        'class' 可添加student,teacher,classrescord
        'course' 可添加classes'''
        need_change = self.set_db(dir,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]#
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value = all_obj_list.index(i)
            i.__dict__[modify_name].append(add_name)
            i.save_db(dir,i,all_obj_list)

    def del_db(self,dir,modify_name,del_name,onlyidname,onlyidvalue):
        need_change = self.set_db(dir,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value_list = i.__dict__[modify_name]
            if index_value_list.count(del_name) != 0:
                del_index = index_value_list.index(del_name)
                index_value_list.pop(del_index)
                i.save_db(dir,i,all_obj_list)
            return None

    def change_db(self,dir,modify_name,before_change,after_change,onlyidname,onlyidvalue):
        need_change = self.set_db(dir,onlyidname,onlyidvalue)
        all_obj_list = need_change[0]
        change_obj_list = need_change[2]
        for i in change_obj_list:
            index_value_list = i.__dict__[modify_name]
            if type(index_value_list) == list:
                if index_value_list.count(before_change) != 0:
                    before_change_index = index_value_list.index(before_change)
                    index_value_list[before_change_index] = after_change
                    i.save_db(dir,i,all_obj_list)
                return None
            else:
                i.__dict__[modify_name] = after_change
                i.save_db(dir,i,all_obj_list)

    def add_teacher(self,dir):
        '''添加老师'''
        student = []
        course_str = self.isname_allobjlist(settings.COURSE_DB_DIR, "老师", "课程")
        course = []
        course.append(course_str)
        classes_str = self.isname_allobjlist(settings.CLASSES_DB_DIR, "老师", "班级")
        classes = []
        classes.append(classes_str)
        school = self.isname_allobjlist(settings.SCHOOL_DB_DIR, "老师", "学校")
        name=input("请输入老师姓名:")
        sex=input("请输入老师性别:")
        age=input("请输入老师年龄:")
        assets=input("请输入老师资产:")
        print("初始化学生:空")
        x = Manager().find_id(settings.SCHOOL_DB_DIR,school,"name")
        if x == []:
            print("学校为空,返回")
            return x
        teacherid = Manager().create_md5()
        teacher_obj = Teacher(name,age,sex,assets,teacherid,student,school,classes,course)
        onlyidvalue = Manager().find_id(settings.TEACHER_DB_DIR,name,"id")
        if onlyidvalue:
            print("该老师已存在")
            return None
        else:
            classidvalue = self.find_id(settings.CLASSES_DB_DIR,str(classes), "classid")  # 检测classid
            self.add_db(settings.CLASSES_DB_DIR, "teacher", name, "classid", classidvalue)
            teacher_obj.save(settings.TEACHER_DB_DIR,teacher_obj)
            return self

    def add_school(self,dir):
        classes = []
        courses = []
        name = input("请输入学校名:")
        addr = input("请输入学校地址:")
        print("初始化班级:空")
        print("初始化课程:空")
        schoolid = Manager().create_md5()
        school_obj = School(name,addr,schoolid,classes,courses)
        onlyidvalue = Manager().find_id(settings.SCHOOL_DB_DIR,name,"schoolid")#检测是否有该学校名称对应的唯一id
        if onlyidvalue:
            print("该学校已存在")
            return None
        else:
            school_obj.save(settings.SCHOOL_DB_DIR, school_obj)
            print("创建成功")
            return self

    def add_classrecord(self):
        name = input("请输入上课记录名称:")
        classes = list(self.isname_allobjlist(settings.CLASSES_DB_DIR, "上课记录", "班级"))
        teacher = self.isname_allobjlist(settings.TEACHER_DB_DIR, "上课记录", "老师")
        section = input("请输入section:")
        coursedate = time.strftime("%Y-%m-%d",time.localtime())
        studyrecord = list(self.isname_allobjlist(settings.STUDYRECORD_DB_DIR, "上课记录", "学习记录"))
        id = self.create_md5()
        classrecord_obj = ClassRecord(name,classes,teacher,section,coursedate,studyrecord,id)
        onlyidvalue = self.find_id(settings.CLASSRECORD_DB_DIR, name, "id")
        if onlyidvalue:
            print("该上课记录已存在")
            return None
        else:
            classrecord_obj.save(settings.CLASSRECORD_DB_DIR, classrecord_obj)
            return self

    def add_studyrecord(self):
        "achievement"
        student = self.isname_allobjlist(settings.CLASSRECORD_DB_DIR,"学习记录", "学生")
        name = input("请输入学习记录名称:")
        sigh_status = "yes"
        sigh_date = time.strftime("%Y-%m-%d",time.localtime())
        section = self.isname_allobjlist2(settings.CLASSRECORD_DB_DIR,"section","学习记录","section")
        id = self.create_md5()
        achievement = None
        studentrecord_obj = StudyRecord(name,sigh_status,sigh_date,student,achievement,section,id)
        onlyidvalue = self.find_id(settings.STUDYRECORD_DB_DIR, name, "id")
        if onlyidvalue:
            print("该学习记录已存在")
            return None
        else:
            studentrecord_obj.save(settings.STUDYRECORD_DB_DIR, studentrecord_obj)
            return self

    def isname_allobjlist2(self,path,ar,arg,args):
        while True:
            allobj_list = self.get_allobj_argname(path, ar)
            print("可增加的{}列表:".format(args), allobj_list)
            obj_name = input("请输入{}所选{}:".format(arg,args))
            if allobj_list:
                if obj_name not in allobj_list:
                    continue
                x = Manager().find_id(path, obj_name,ar)
                if x == []:
                    print("{}为空,返回".format(args))
                    return x
                return obj_name
            return obj_name
    def isname_allobjlist(self,path,arg,args):
        while True:
            allobj_list = self.get_allobj_argname(path, "name")
            print("可增加的{}列表:".format(args), allobj_list)
            obj_name = input("请输入{}所选{}:".format(arg,args))
            if allobj_list:
                if obj_name not in allobj_list:
                    continue
                x = Manager().find_id(path, obj_name, "name")
                if x == []:
                    print("{}为空,返回".format(args))
                    return x
                return obj_name
            return obj_name

    def add_student(self,dir):
        teacher = list(self.isname_allobjlist(settings.TEACHER_DB_DIR,"学生","老师"))
        school = self.isname_allobjlist(settings.SCHOOL_DB_DIR,"学生","学校")
        classes = self.isname_allobjlist(settings.CLASSES_DB_DIR,"学生","班级")
        course = self.isname_allobjlist(settings.COURSE_DB_DIR, "学生", "课程")
        course = list(course)
        if school or classes or course:
            name = input("请输入学生姓名:")
            sex = input("请输入学生性别:")
            age = input("请输入学生年龄:")
            studentid = Manager().create_md5()
            student_obj = Student(name,sex,age,studentid,teacher,school,classes,course)
            onlyidvalue = Manager().find_id(settings.SCHOOL_DB_DIR, name,"studentid")  # 检测是否有该学校名称对应的唯一id
            if onlyidvalue:
                print("该学生已存在")
            else:
                teacheridvalue = self.find_id(settings.TEACHER_DB_DIR, teacher, "id")  # 检测schoolid
                self.add_db(settings.TEACHER_DB_DIR, "student", name, "id", teacheridvalue)
                student_obj.save(settings.STUDENT_DB_DIR,student_obj)
                return self
        else:
            return [school,classes,course]

    def add_the_class(self,dir):
        '''创建班级'''
        student = []
        teacher = []
        classrescord = []
        allobjschool_list = self.get_allobj_argname(settings.SCHOOL_DB_DIR, "name")
        print("可增加的学校列表:", allobjschool_list)
        school = input("请输入老师学校:")
        x = Manager().find_id(settings.SCHOOL_DB_DIR, school, "name")
        if x == []:
            print("学校为空,返回")
            return x
        name = input("请输入班级名:")
        semester = input("请输入学期:")
        allobj_list = self.get_allobj_argname(settings.COURSE_DB_DIR,"name")
        print("可增加的课程列表:",allobj_list)
        course = input("请输入课程:")
        course_find = self.find_id(settings.COURSE_DB_DIR, course, "name")
        if course_find == []:
            print("您输入课程有误，返回")
            return course_find
        date = input("请输入开课日期:")
        print("初始化老师:空")
        print("初始化学生:空")
        print("初始化班级记录:空")
        classid = Manager().create_md5()
        the_class = Classes(name,semester,course,date,classid,student,teacher,classrescord,school)
        classidvalue = self.find_id(settings.CLASSES_DB_DIR, name, "classid")  # 检测是否有该学校名称对应的唯一id
        courseidvalue = self.find_id(settings.COURSE_DB_DIR,course,"courseid")
        schoolidvalue = self.find_id(settings.SCHOOL_DB_DIR,school,"schoolid")#检测schoolid
        self.add_db(settings.SCHOOL_DB_DIR,"classes",name,"schoolid",schoolidvalue)
        self.add_db(settings.COURSE_DB_DIR,"classes",name,"courseid",courseidvalue)
        if classidvalue:
            print("该班级已存在")
        else:
            the_class.save(settings.CLASSES_DB_DIR,the_class)
            return self

    def add_course(self,dir):
        school = self.isname_allobjlist(settings.SCHOOL_DB_DIR, "课程", "学校")
        classes = self.isname_allobjlist(settings.CLASSES_DB_DIR, "课程", "班级")
        teacher = list(self.isname_allobjlist(settings.TEACHER_DB_DIR,"课程","老师"))
        name = input("请输入课程名:")
        period = input("请输入学期:")
        price = input("请输入价格:")
        outline = input("请输入大纲:")
        #x = Manager().find_id(settings.SCHOOL_DB_DIR, school, "name")#查找学校
        y = Manager().find_id(settings.COURSE_DB_DIR, name, "name")#查找课程
        schoolidvalue = self.find_id(settings.SCHOOL_DB_DIR, school, "schoolid")  # 检测schoolid
        self.add_db(settings.SCHOOL_DB_DIR, "courses", name, "schoolid", schoolidvalue)
        if school == [] or teacher == []:
            print("学校或老师为空,返回")
            return [school,teacher]
        if y == name:
            print("改课程已存在,返回重建")
            return y
        else:
            courseid = Manager().create_md5()
            course = Courses(name, courseid, period, price, outline, classes, school,teacher)
            course.save(settings.COURSE_DB_DIR,course)
            return self

    def get_allobj_list(self,dir):
        obj_list = []
        obj_dic = {}
        all_obj_list = self.get_name(dir)
        if all_obj_list:
            for i in all_obj_list:
                if i:
                    obj_dic[i] = i.__dict__
            return obj_dic
        return None

    def get_allobj_argname(self,path,argname):
        allobj_dict = self.get_allobj_list(path)
        dic = []
        for key,value in allobj_dict.items():
            dic.append(value[argname])
        return dic

    def common_info(self,arg,num):
        for mem_num,mem_value in self.dict_all_value.items():
            if mem_num != num:
                print(mem_num ,"{}{}".format(arg,mem_value[0]))
            else:
                print(mem_num ,mem_value[0])
        while True:
            input_num = input("请输入序号:")
            if not input_num or not input_num.isdigit():
                continue
            input_num = int(input_num)
            if input_num not in self.dict_all_value.keys():
                continue
            if input_num == num:
                return None
            return input_num

    def look_info1(self,path,input_num):
        ###查看的方法
        # while True:

        if input_num:
            #path = self.dict_all_value[input_num][1]
            value_list = []
            x = Admin_ser().get_allobj_list(path)
            if x == None:
                return input_num
            choose_list = self.dict_all_value[input_num][2]
            z = PrettyTable(choose_list)
            for key, value in x.items():
                display_list = []
                value_list.append(value["name"])
                z.align["name"] = "l"
                z.padding_width = 2
                for i in choose_list:
                    display_list.append(value[i])
                z.add_row(display_list)
            print("\033[30;1m{}\033[0m".format(z))
            return input_num
        return None

    def look_info(self,arg,):
        ###查看的方法
        # while True:
            input_num = self.common_info(arg,8)
            if input_num:
                path = self.dict_all_value[input_num][1]
                value_list = []
                x = Admin_ser().get_allobj_list(path)
                if x == None:
                    return input_num
                choose_list = self.dict_all_value[input_num][2]
                z = PrettyTable(choose_list)
                for key, value in x.items():
                    display_list = []
                    value_list.append(value["name"])
                    z.align["name"] = "l"
                    z.padding_width = 2
                    for i in choose_list:
                        display_list.append(value[i])
                    z.add_row(display_list)
                print("\033[30;1m{}\033[0m".format(z))
                return input_num
            return None

    def change_list1(self,arg_num,path,):
        count = 0
        dic = {}
        for i in self.dict_all_value[arg_num][3]:
            count += 1
            dic[count] = i
        #x = self.get_allobj_list(path)
        could_change_list = self.dict_all_value[arg_num][6]
        count = 0
        print("可以更改的名称")
        onlyidname = self.dict_all_value[arg_num][2][-1]
        onlyidvalue = input("请输入要修改的{}:".format(onlyidname))
        change_obj_dic=self.grep_db(path,onlyidname, onlyidvalue)
        dic2 = {}
        for change_value in could_change_list:
            count += 1
            dic2[count]=change_value
            print(count,change_value)
        change_num = int(input("请输入可以更改的序号:"))
        modify_name = dic2[change_num]
        before_change = change_obj_dic[modify_name]
        print("该{}的更改之前的名字为{}".format(onlyidvalue,before_change))
        after_change = input("请输入修改后的{}名称:".format(modify_name))
        self.change_db(path,modify_name, before_change, after_change, onlyidname, onlyidvalue)
        print("更改成功")
        return 1

    def change_list(self,arg_num,path):
        count = 0
        dic = {}
        for i in self.dict_all_value[arg_num][3]:
            count += 1
            dic[count] = i
        #x = self.get_allobj_list(path)
        could_change_list = self.dict_all_value[arg_num][4]
        count = 0
        print("可以更改的名称")
        onlyidname = self.dict_all_value[arg_num][2][-1]
        onlyidvalue = input("请输入要修改的{}:".format(onlyidname))
        change_obj_dic=self.grep_db(path,onlyidname, onlyidvalue)
        dic2 = {}
        for change_value in could_change_list:
            count += 1
            dic2[count]=change_value
            print(count,change_value)
        change_num = int(input("请输入可以更改的序号:"))
        modify_name = dic2[change_num]
        before_change = change_obj_dic[modify_name]
        print("该{}的更改之前的{}为{}".format(onlyidvalue,modify_name,before_change))
        after_change = input("请输入修改后的{}名称:".format(modify_name))
        self.change_db(path,modify_name, before_change, after_change, onlyidname, onlyidvalue)
        print("更改成功")
        return 1

    def add_list(self,arg_num,path):
        ###添加方法
        dic_obj_path={
            "student":settings.STUDENT_DB_DIR,
         "classes":settings.CLASSES_DB_DIR,
         "course":settings.COURSE_DB_DIR,
         "teacher":settings.TEACHER_DB_DIR,
         "classrescord":settings.CLASSRECORD_DB_DIR,
        "studyrecord":settings.STUDYRECORD_DB_DIR}
        count = 0
        dic = {}
        for i in self.dict_all_value[arg_num][3]:
            count += 1
            dic[count] = i
        x = self.get_allobj_list(path)
        could_change_list = self.dict_all_value[arg_num][3]
        count = 0
        print("可以更改的名称")
        onlyidname = self.dict_all_value[arg_num][2][-1]
        onlyidvalue = input("请输入要修改的{}:".format(onlyidname))
        #change_obj_dic = self.grep_db(path, dict_all_value[arg_num][2][-1], onlyidvalue)
        dic2 = {}
        for change_value in could_change_list:
            count += 1
            dic2[count] = change_value
            print(count, change_value)
        change_num = int(input("请输入可以更改的序号:"))
        modify_name = dic2[change_num]
        q = self.get_name(dic_obj_path[modify_name])
        print("可以增加的{}:".format(modify_name))
        for k  in q:
            if k:
                print(k.__dict__["name"])
        if q == [None,None]:
            print("检测没有{}，返回".format(modify_name))
            return 3

        add_name = input("请输入新增加的{}名称:".format(modify_name))
        for z in q:
            if z:
                print(z.__dict__["name"])
                if z.__dict__["name"] == add_name:
                    print("{}存在，正在添加".format(add_name))
                    self.add_db(path, modify_name, add_name, onlyidname, onlyidvalue)
                    print("增加成功")
                    return 1
            continue
        print("{}中{}不存在，无法加入".format(modify_name,add_name))
        return 2

    def look_info_(self,arg):
        #查看调用接口     功能ok
        while True:
            x = self.look_info(arg)
            if x:
                continue
            break

    def change_info(self):
        ###更改调用接口   功能ok
        while True:
            input_num = self.look_info("更改")
            if input_num:
                path = self.dict_all_value[input_num][1]
                menu = '''
                            1.  \033[30;1m添加项（{}）\033[0m
                            2.  \033[31;1m更改项（{}）\033[0m
                            3.  \033[32;1m后退\033[0m
                            '''.format(self.dict_all_value[input_num][3],self.dict_all_value[input_num][4])
                menu_dic = {
                    '1': 'self.add_list({},r"{}")'.format(input_num,path),
                    '2': 'self.change_list({},r"{}")'.format(input_num,path),
                    '3': 'None'}
                value_list = []
                exit_flag = self.interactive(menu,menu_dic)
                if exit_flag == None:
                    return exit_flag
                if exit_flag == 1:
                    continue
            break

            # self.change_db(path, modify_name, before_change, after_change, onlyidname, onlyidvalue)

    def add_info(self):
        while True:
            input_num = self.look_info("添加")
            if input_num:
                path = self.dict_all_value[input_num][1]
                func_name = self.dict_all_value[input_num][5]
                x = eval(func_name)(path)
                return x
            break

    def del_info(self):
        ###删除方法
        while True:
            input_num = self.look_info("删除")
            if input_num:
                path = self.dict_all_value[input_num][1]
                func_name = self.dict_all_value[input_num][5]
                x = eval(func_name)(path)
                print(x)
            break

    def logout(self):
        exit(" 谢谢使用 ".center(50, "#"))


#print(look_info(settings.SCHOOL_DB_DIR))

#x = Admin_ser().add_course()
# "老北京增加"
#Admin_ser().add_db(settings.SCHOOL_DB_DIR,"courses","linux","schoolid","22046ae04a62cf4618ac71952186366a")
# x = Admin_ser().find_id(settings.SCHOOL_DB_DIR,"niuybi","schoolid")
# print(x)

# 查询
# x = Admin_ser().get_allobj_list(settings.SCHOOL_DB_DIR)
# print(x)
# if x[1]["name"] == "niuybi":
#     print("ok")
# for i in x[1]:
#     if i["name"] == "niuybi":
#         print(i)
#         print(x[0])

# for (key,value) in x.items():
#     if value["name"] == "niuybi":
#         print(key,value)


def oo(dir,findname,findkey,value):
    ''''''
    ii = Admin_ser().grep_obj(dir, findname)[1][findkey]
    if type(ii)  == list:
        for value in ii:
            print("{}已存在".format(value))
            return value
        return value
    else:
        if type(ii) == str:
            if value == ii:
                print("{}已存在".format(value))
                return value
            return value


# print(grep_obj(settings.COURSE_DB_DIR,"niuybi")[0])
#y = oo(settings.SCHOOL_DB_DIR,"niuybi","classes","niuybi")
# z = Admin_ser().grep_obj(settings.CLASSES_DB_DIR,"niuybi")
# print(z)
#Admin_ser().add_the_class([],[],[])

# x = Admin_ser().get_allobj_list(settings.CLASSES_DB_DIR)
# print(x)

