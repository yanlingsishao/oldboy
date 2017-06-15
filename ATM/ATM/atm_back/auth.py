#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import manager
#装饰器模块

# common 存款，取款，查询余额，修改密码，转账，账单打印
def auth_common_permissions(func):
    def wrapper(*args, **kwargs):
        user_status = manager.get_user_onevalue(*args,"user_status")
        if user_status == "lockuser":
            print("没有权限")
            return False
        else:
            re = func(*args, **kwargs)
            return re
    return wrapper

#
#借款
def auth_huabei_permissions(func):
    def wrapper(*args, **kwargs):
        user_status = manager.get_user_onevalue(*args,"user_status")
        if user_status == "huabei":
            re = func(*args, **kwargs)
            return re
        else:
            print("没有权限")
            return False
    return wrapper

# 还款