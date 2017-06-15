#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年6月2日
@author: WangQiyuan

'''
user_list=[
    {"name":"wangqiyuan","passwd":"123"},
    {"name":"wupeiqi","passwd":"12365"},
    {"name":"alex","passwd":"12c3"},
    {"name":"linhaifeng","passwd":"1000.0"},
]

current_user={"username":None,"login":False}

def auth_demo(func):
    def wrapper(*args,**kwargs):
        if current_user["username"] and current_user["login"]:
            res = func(*args,**kwargs)
            return res
        username=input(">>>用户名：").strip()
        passwd=input(">>>密码：").strip()

        for index,user_dic in enumerate(user_list):
            print(user_dic)
            if username == user_dic["name"] and passwd == user_dic["passwd"]:
                current_user["username"]=username
                current_user["login"]=True
                res=func(*args,**kwargs)
                return res
        else:
            print("用户名或者密码不正确")
    return wrapper

def index():
    print("欢迎来到主页面")

@auth_demo
def home():
    print("这里是你家")

def shopping_car():
    print("查看购物车啊亲")

def order():
    print("查看订单啊亲")

home()
