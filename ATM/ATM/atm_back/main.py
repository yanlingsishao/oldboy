#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import login

def Exit():
    print("程序退出")
    exit()

def Main():
    msg='''
        欢迎来到：
            1:登录
            2:退出'''
    msg_dic = {
        "1":login.login_user,
        "2":Exit,
    }
    while True:
        print(msg)
        choice = input("请输入你的选项：").strip()
        if choice not in msg_dic.keys(): continue
        res=msg_dic[choice]()


if __name__ == "__main__":
    Main()

