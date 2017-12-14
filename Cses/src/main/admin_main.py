#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''

'''管理员
    查看                  学校---[课程,班级]
    选择                  课程---[班级]
    更改                  班级---[学生、老师、班级记录]
    创建                  学生---[老师]
    删除                  老师---[学生]'''

import os,sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# sys.path.append("..")
# sys.path.append("../..")
# from bin import start
from services.admin_ser import Admin_ser
from conf import settings


class Admin_view(Admin_ser):
    def __init__(self):
        Admin_ser.__init__(self)

    def auth(self, username, password):
        admin_file = settings.ADMIN_AUTH_DB
        if os.path.isfile(admin_file):
            with open(admin_file, 'r') as f:
                admin_data = json.load(f)
            if admin_data["name"] == username and admin_data["password"] == password:
                return True
            else:
                print("用户名或密码错误")

    def system_manager(self):
        '''
        管理系统
        :return:
        '''
        menu = '''
    ----------------- 欢迎进入管理系统 -----------------
        1.  \033[30;1m查看\033[0m
        2.  \033[31;1m更改\033[0m
        3.  \033[32;1m创建\033[0m
        4.  \033[34;1m后退(注销)\033[0m
    --------------------------------------------------
        '''
        menu_dic = {
            '1': 'Admin_ser().look_info_("查看")',
            '2': 'Admin_ser().change_info()',
            '3': 'Admin_ser().add_info()',
            '4': 'Admin_ser().ret()'
        }
        username = input("输入用户名:").strip()
        password = input("输入密码:").strip()
        auth = self.auth(username, password)
        while True:
            if auth:
                x = Admin_ser().interactive(menu, menu_dic)
                if x == None:
                    x = Admin_ser().interactive(menu, menu_dic)
                if x == 0:
                    return x
                continue

def look_info(dir):
    print("请输入")
    value_list = []
    x = Admin_ser().get_allobj_list(dir)
    for key, value in x.items():
        value_list.append(value["name"])
    return value_list




    # admin_page()
    #print(look_info(settings.CLASSES_DB_DIR))