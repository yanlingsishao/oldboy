#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-11 17:11
# @Author  : Jerry Wang
# @Site    : 
# @File    : user_reg.py
# @Software: PyCharm

import configparser
import os ,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取相对路径转为绝对路径赋于变量
sys.path.append(BASE_DIR)#增加环境变量

from conf import config
#修改个信息 磁盘大小
def set_info(gr_name,addse,name,pwd,ports):
    config_info=configparser.ConfigParser()#读数据
    file_dir="%s%s"%(config.AUTH_FILE,gr_name)#主机组用户名密码文件路径

    config_info[addse]={}#ip 主机
    config_info.set(addse,config.USER,name)#用户
    config_info.set(addse,config.PWD,pwd)#密码
    config_info.set(addse,config.PORTS,ports)#端口
    with open(file_dir,"a+") as f:
        config_info.write(f)#写入文件
    #config_info.write(open(file_dir,‘a‘))#写入文件
    print("创建完成".center(60,"="))
    print("组：【%s】\nIP:[%s]\n用户名:[%s]\n密码:[%s]\n端口:[%s]"%(gr_name,addse,name,pwd,ports))

if __name__ == "__main__":

    gr_name=input("组名：")#组
    addse=input("IP地址:")#ip地址
    name=input("用户名:")#用户
    pwd=input("密码:")#密码
    ports=input("端口:")#端口
    set_info(gr_name,addse,name,pwd,ports)