#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import json


def loadFont():#获取json
    province_json = open("省市.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(province_json)
    province_json.close()  #注意多重结构的读取语法
    return setting

#loadFont().keys()第一级目录
#loadFont().get(x)第二级目录
#loadFont().get(x).get(y)第三级目录

def login_tr_menu():##三级入口
    num = 0#状态码，0仍在循环，1即跳出循环
    while True:
        print("全国省份：")
        province = loadFont().keys()#获取所有省份
        for i in province:
            print(i)#将所有省份逐行打印
        prov_input = input("please input your Province:")

        if prov_input in province:
            city = loadFont().get(prov_input).keys()  # 获取第二级目录
            for u in city:#将所有市逐行打印
                print(u)
        else:
            print("抱歉，没有查到此省信息，请重新输入")
            continue
        if num == 0:
            while True:
                city_input = input("please input your City（x:返回上级，q：退出）:")#输入城市
                if city_input == "x":#x值，返回上级
                    break
                elif city_input == "q":#q值，先改变状态码，跳出此循环，根据状态码，可以跳出外面的循环
                    num = 1
                    break
                else:
                    if city_input in loadFont().get(prov_input):
                        county = loadFont().get(prov_input).get(city_input)#获取县级
                        for p in county:#将所有县区逐行打印
                            print(p)
                    else:
                        print("没有查询到此城市，请重新输入")
                        continue
        if num == 1:#跳板，跳出循环
            break
        else:
            continue



if __name__ == "__main__":
    login_tr_menu()