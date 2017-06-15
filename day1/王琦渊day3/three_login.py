#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月10日
@author: WangQiyuan
'''
user_list = {"wangqiyuan":"123456",
             "liming":"123456"
             }


def login():#登录入口
    count = 0#计数器，初始count=0
    while True:
        user = input("please input your name:")
        if user in user_list.keys():#验证用户是否存在
            isnot_blacklist(user,count)#存在，然后去验证用户是否被锁
        else:
            print("无此用户，请重新输入：")
            continue

def isnot_blacklist(user,count):#验证锁定
    lock_file = open('user_lock', 'r')#读，打开锁定文件
    lock_list=[]#设定锁定列表，初始为空
    for x in lock_file:#将锁定文件每行赋值给x
        lock_list.append(x.strip())#每次锁定列表往里面加一个去除前后空白的x
    lock_file.close()#关闭文件

    if user in lock_list:#验证用户是否在锁定列表
        print("抱歉，您的账号已被锁定")#用户在黑名单中
        exit()#退出程序
    else:
        isnot_passwd(user,count)#不在，则去密码输入方法

def join_blacklist(user):#加入黑名单方法
    lock_file = open('user_lock', 'a')#打开锁定文件，append方式
    lock_file.write(user + "\n")#写入用户，并且换行
    lock_file.close()#关闭文件

def isnot_passwd(user,count):#验证密码方法
    while True:
        pass_input = input("please input your password:")#输入密码
        if count > 2:#计数count>2
            join_blacklist(user)#即加入黑名单将此用户
            print("用户已锁定")
            exit()#退出程序
        if pass_input == user_list.get(user):#判断密码是否正确
            print("login success")#正确，打印成功
            exit()#退出程序
        else:#密码不正确
            print("passwd is not success")
            count += 1#计数加1
            continue




if __name__ == "__main__":
    login()






