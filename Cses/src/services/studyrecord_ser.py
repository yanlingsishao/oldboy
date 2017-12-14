#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-13 10:45
# @Author  : Jerry Wang
# @Site    : 
# @File    : studyrecord_ser.py
# @Software: PyCharm
import sys
import time
sys.path.append("..")
sys.path.append("../..")
from conf import settings
from services.manager_ser import Manager
class StudyRecord(Manager):
    def __init__(self,name,sigh_status,sigh_date,student,achievement,section,id):
        '''sigh_status,sigh_date,student,achievement,section
        签到状态，签到日期，学生，成绩，节次
        {节次:{学生:[签到状态,成绩,签到日期]}}
        '''

        self.name = name
        self.student = student
        self.sigh_status = sigh_status
        self.sigh_date = sigh_date
        self.achievement = achievement
        self.section = section
        self.id = id

'''
方法
    1：取出studyrecord对象 ----
    2：增加studyrecord对象 ----检测section
    3：删除studyrecord对象
    4: 修改studyrecord对象    1、签到状态 2、签到时间  3、成绩
'''

class StudyRecordSer(Manager):
    def get_studyrecord_obj(self,section):
        "根据section，返回列表对象"
        all_obj = self.get_name(settings.STUDYRECORD_DB_DIR)
        for i in all_obj:
            if i:
                if i.__dict__["section"] == section:
                    return i
                return None
            continue
        return None

    def check_section(self):
        pass

    def add_studyrecord_obj(self,student,section):
        x = input("请输入签到")
        if x == "签到":
            sigh_status = True
            sigh_date = time.sigh_date = time.strftime("%Y-%m-%d %X")
            achievement = None
            id = Manager().create_md5()
            obj = StudyRecord(sigh_status,sigh_date,student,achievement,section)
            onlyidvalue = Manager().find_id(settings.STUDYRECORD_DB_DIR,student,"id")
            if onlyidvalue:
                print("该学习记录已存在")
            else:
                obj.save(settings.STUDYRECORD_DB_DIR, obj)
                return self
        else:
            print("签到失败")
            return None

    def del_studyrecord_obj(self):
        pass

    def change_studyrecord_obj(self):
        pass

# x = StudyRecord("1",2,3,4,5)
# print(x.__dict__)
#{'lala': {5: {2: ['1', 3, 4]}}}

# x = StudyRecordSer().get_studyrecord_obj("1")
# print(x)

# 查看
z = StudyRecordSer().get_studyrecord_obj("第二节")
print(z)

# z = StudyRecordSer().add_studyrecord_obj("wangqiyuan","第二节")
# print(z)