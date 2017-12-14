#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年6月7日
@author: WangQiyuan

'''
'''
账号的方法
    1、增加账号   ok
    2、删除账号   ok
    3、账号权限
    4、冻结账号
    5、解锁账号
最开始菜单：开户、登录、退出
普通用户状态：common：
            存款，取款，查询余额，修改密码，转账，账单打印
花呗用户状态：huabei：
            common权限，借款，还款，账单发邮箱
逾期用户状态：overdue
            common权限，还款，账单发邮箱
冻结用户状态：lockuser：
            无权限
'''
import sys
import os
sys.path.append(os.path.dirname(__file__))

import configparser
import actions
import manager
import userfunction
from logger import MyLogger


CONFIG_FILE = '..\\data\\user_info\\config.cfg'
USER_INFO = "..\\data\\user_info\\"

class validate():#验证功能
    def validate_begin_user():  # 验证开户名
        while True:
            username = input("请输入开户名:")
            ret = manager.isnot_username(username)
            if ret == True:
                print("此用户名太受欢迎,请更换一个")
                MyLogger.warning("此用户名太受欢迎,请更换一个")
                continue
            elif ret == False:
                print("开户名可用")
                MyLogger.info("开户名【{}】可用".format(username))
                return username

    def validate_pass():  # 验证密码
        while True:
            passwd = input("请输入密码:")
            two_passwd = input("确认密码:")
            if passwd == two_passwd:
                MyLogger.info("密码验证一致")
                return passwd
            else:
                MyLogger.warning("两次密码不一致！！！")
                print("两次密码不一致！！！")

    def validate_phone():  # 验证手机
        while True:
            try:
                phone = input("请输入手机号码:")
                ret = manager.isnot_phone(phone)
                if ret == True:
                    print("注册手机已被使用!")
                    continue
                elif ret == False and len(phone) == 11:
                    phone = int(phone)
                    return phone
                else:
                    print("手机号码格式不正确")
            except ValueError:
                print("手机号码格式不正确")
                continue

def add_user():#开户功能
    username=validate.validate_begin_user()
    passwd=validate.validate_pass()
    phone=validate.validate_phone()
    print(("用户 {} 信息输入成功，等待出卡。。。".format(username)))
    MyLogger.info("用户 【{}】 信息输入成功，等待出卡。。。".format(username))
    manager.add_user_info(username,passwd,phone)
    print("用户 {} 出卡成功，打印凭条".format(username))
    MyLogger.info("用户 【{}】 出卡成功，打印凭条".format(username))
    account_user_info=manager.fetch_single_user_info(username)
    print(account_user_info)#在外层写个打印凭条
    return account_user_info













