#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''


import os
import manager
import userfunction



def login_user():
    username=userfunction.login_begin_user()
    user_cardid=userfunction.login_begin_cardid(username)
    user_pass=userfunction.login_begin_pass(username)
    userstatus=manager.get_user_onevalue(username,"user_status")
    #common_dic=userfunction.huabei_rule(username, userstatus)
    #login_dic=userfunction.login_use(username, userstatus)
    #msg_dic=userfunction.all_rule(username)
    while True:
        str_show = userfunction.get_all_strdic(username,userstatus)
        choice = input("请输入您的操作：")
        if choice == "":continue
        elif userfunction.get_rule_func(int(choice),userstatus) == False:
            break
        elif userfunction.get_all_strdic_func(username,userstatus).get(int(choice)) == "修改密码":
             userfunction.get_rule_func(int(choice), userstatus)(username)
             break
        elif int(choice) not in str_show.keys():continue
        else:
            num = userfunction.get_rule_func(int(choice), userstatus)(username)




# login_user()