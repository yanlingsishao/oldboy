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

class Student_view:
    def sigh(self):
        k = Admin_ser().look_info1(settings.STUDYRECORD_DB_DIR,7)
        x = Admin_ser().change_list(7, settings.STUDYRECORD_DB_DIR)

    def add_studyrecord(self):
        x = Admin_ser().add_studyrecord()

    def look_studyrecord(self):
        k = Admin_ser().look_info1(settings.STUDYRECORD_DB_DIR,7)

    def login(self):
        menu = u'''
        ------- 欢迎进入学生管理视图 ---------
        \033[32;1m 1.  更改签到状态
        2.  添加学习记录
        3.  查看学习记录
        4.  返回
        \033[0m'''
        path = settings.STUDYRECORD_DB_DIR
        menu_dic = {
            '1': self.sigh,
            '2': self.add_studyrecord,
            '3': self.look_studyrecord,
            '4': "logout",
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                option = input("请选择：").strip()
                if option in menu_dic:
                    if int(option) == 4:
                        exit_flag = True
                    else:
                        menu_dic[option]()
                else:
                    print("\033[31;1m输入错误，重新输入\033[0m")
