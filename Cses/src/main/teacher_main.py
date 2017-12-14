#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import time
import os,sys
from prettytable import PrettyTable

sys.path.append("..")
sys.path.append("../..")
from services.admin_ser import Admin_ser
from conf import settings

class Teacher_view:
    def add_studyachievement(self):
        k = Admin_ser().look_info1(settings.STUDYRECORD_DB_DIR,7)
        Admin_ser().change_list1(7, settings.STUDYRECORD_DB_DIR)

    def add_classrecord(self):
        x = Admin_ser().add_classrecord()

    def look_classrecord(self):
        k = Admin_ser().look_info1(settings.CLASSRECORD_DB_DIR,6)

    def add_classstudyrecord(self):
        k = Admin_ser().look_info1(settings.CLASSRECORD_DB_DIR, 6)
        x = Admin_ser().add_list(6, settings.CLASSRECORD_DB_DIR)

    def login(self):
        menu = u'''
        ------- 欢迎进入老师管理视图 ---------
        \033[32;1m 1.  添加上课记录
        2.  查看上课记录
        3.  增加studyrecord
        4.  更改学生成绩
        5.  返回
        \033[0m'''
        path = settings.STUDYRECORD_DB_DIR
        menu_dic = {
            '1': self.add_classrecord,
            '2': self.look_classrecord,
            '3': self.add_classstudyrecord,
            '4': self.add_studyachievement,
            '5': "logout",
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 5:
                        exit_flag = True
                    else:
                        menu_dic[option]()
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")


