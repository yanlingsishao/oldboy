#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
'''
#账号状态
普通用户状态：common：
            存款，取款，查询余额，修改密码，转账，账单打印
花呗用户状态：huabei：
            common权限，借款，还款，
逾期用户状态：overdue
            common权限，还款，账单发邮箱
冻结用户状态：lockuser：
            无权限
#花呗模块，功能
1、账号定期还款
    每月8号开始还款，还款失败，则更改账号status为逾期状态
2、定期账单
    还款后的的账单发送邮件给用户
3、借款。
4、逾期还款，
    超出一个月，账号冻结，1-30天之内，每10天加一次息。1--10，一共收借款的0.1。11--20，一共收借款的0.2  21--30，一共收借款的0.3
5、逾期
'''
import manager

def auth_demo(func):
    def wrapper(*args,**kwargs):
        user_status=manager.get_user_onevalue("wangqiyuan","user_status")
        if user_status == "common":
            print("没有权限")

        else:
            return user_status


