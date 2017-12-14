#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
#ATM管理系统
'''
--------功能--------
2、指定用户额度
4、账号定期还款
6、定期账单

--------方法---------
账号的方法
    1、增加账号
    2、删除账号
    3、账号权限
    4、冻结账号
    5、解锁账号
-------模块----------
    1、#auth模块



--------------------
'''
import os
import configparser
import actions
import manager
from prettytable import PrettyTable

CONFIG_FILE = '..\\data\\user_info\\config.cfg'
ADM_CONFIG_FILE = '..\\data\\user_info\\adm.cfg'
USER_INFO = "..\\data\\user_info\\"

def Esxi():
    exit()


def adm_main():
    msg = '''
    欢迎来到管理界面：
        1、删除用户
        2、所有用户查看
        3、解锁用户
        4、退出管理
        '''
    msg_dic = {
        #"1": add_user,
        "1": del_user,
        "2": manager.fetch_users,
        "3": unlock_user,
    }
    while True:
        print(msg)
        choice=input("请输入您的操作：")
        if choice == "4": break
        if choice not in msg_dic.keys(): continue
        res = msg_dic[choice]()



#增加用户
def add_user():
    new_user_value=manager.get_option_value()
    new_user=input("增加一个用户：")
    manager.add_one_option(new_user,new_user_value)
    with manager.change_user_info_file(new_user_value) as file:
        file.write("username:{}\n".format(new_user))
        file.write("passwd:e10adc3949ba59abbe56e057f20f883e",)
        file.flush()

#删除用户
def del_user():
    wil_del_user=input("请输入您想要删除的用户：")
    all_user=manager.__cfg()[1]
    if wil_del_user not in all_user:
        print("无此用户")
    else:
        config=configparser.ConfigParser()
        config.read(CONFIG_FILE)
        config.remove_section(wil_del_user)
        config.write(open(CONFIG_FILE, "w"))
        print("删除成功")
    return wil_del_user

#查找用户
# def fetch_user():
#     user_all=cfg_read()
#     count=0
#     user_list = PrettyTable(["ID", "name", "CardID", "status"])  # ！！！留了一个status
#     user_list.align["ID"] = "l"
#     user_list.padding_width = 1
#     for i in user_all:
#         value=get_option_old_value(i)#cardid值
#         user_list.add_row([count,i,value,"running"])
#         count+=1
#     print(user_list)

# 解锁用户
def unlock_user():
    unlock_user_info=input("请输入要解锁的账号:")
    all_user = manager.__cfg()[1]
    if unlock_user_info not in all_user:
        print("无此用户")
    else:
        manager.change_user_info(unlock_user_info,"user_status","common")
        print("解锁成功")
# 退出程序




# 验证用户接口




# if __name__ == "__main__":
#     adm_main()
