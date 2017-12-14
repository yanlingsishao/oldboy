#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年6月6日
@author: WangQiyuan

'''
#！！！这是登录模块
#主要完成功能为：当用户开始使用本系统，进入登陆模块。屏幕显示菜单提示，用户可根据
#需要选择相应功能。具体如下：开户 、存款 、取款 、查询余额 、修改密码 、转账
import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from atm_back import account
from atm_back import login
from atm_back import admin

def login_atm():

    msg_overdue = '''
            1、开户
            2、登录
            3、管理
               '''
    dic_login_atm={
        "1":account.add_user,
        "2":login.login_user,
        "3":admin.adm_main,
    }
    while True:
        print("欢迎来到One Piece".center(50, "*"))
        print(msg_overdue)

        choice = input("请输入您的操作：")
        if choice not in dic_login_atm.keys(): continue
        res = dic_login_atm[choice]()



if __name__ == "__main__":
    login_atm()


