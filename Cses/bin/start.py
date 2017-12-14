#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import sys,os

#程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)
from src.main.admin_main import Admin_view
from src.main.student_main import Student_view
from src.main.teacher_main import Teacher_view

def start():
    menu = '''
       ----------------- 欢迎进入选课系统 -----------------
           1.  \033[30;1m管理界面\033[0m
           2.  \033[31;1m老师界面\033[0m
           3.  \033[32;1m学生\033[0m
           4.  \033[34;1m后退(注销)\033[0m
       --------------------------------------------------
           '''
    menu_dic = {
        '1': Admin_view().system_manager,
        '2': Student_view().login,
        '3': Teacher_view().login,
        '4': exit
    }
    while True:
        print(menu)
        x = input(">>")
        if x:
            z = menu_dic[x]()
            if z == 0:
                continue

if __name__ == "__main__":
    start()