#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-8 17:07
# @Author  : Jerry Wang
# @Site    : 
# @File    : FileHandle.py
# @Software: PyCharm
# @What    : 文件操作
import os,sys
import configparser
from fabric.api import *
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取相对路径转为绝对路径赋于变量
sys.path.append(BASE_DIR)#增加环境变量
from conf import config


x = os.path.abspath("../file")

class FileHand(object):
    def __init__(self,gr_name):  # 组名
        self.gr_name = '%s%s' % (config.AUTH_FILE, gr_name)  # 主机组用户名密码文件路径
        self.config_info = configparser.ConfigParser()  # 读数据对象
        self.name_l = []

    def group_open(self):#打开组文件
        self.config_info.read(self.gr_name)#读取文件
        for i in range(len(self.config_info.sections())):
            self.name_l.append(self.config_info.sections()[i])#信息添加到列表
        else:
            print('主机列表:'.center(40,'='))
            for i in self.name_l:
                print(('[%s]'%i).center(40,' '))

    def inst_attr(self,inst):#获取指令
        self.instruction=inst
        self.attr=self.instruction.split()
        self.inst_a=self.attr[0]

    def upload_file(own_dir,end_dir):
        '''
            eg:
                fab -f FileHandle.py upload_file:own_dir="test",end_dir="/opt"
            传入多个参数
                fab -f FileHandle.py upload_file:own_dir="ExecCmd.py",end_dir="/root"
        '''
        put("../file/UPFILE/%s"%own_dir,"%s"%end_dir)
        run("ls -l %s"%end_dir)

    def download_file(end_dir,end_file):
        '''
            eg:
                fab -f FileHandle.py download_file:end_dir="/root/",end_file="test“
        '''
        get("%s%s"%(end_dir,end_file),"../file/DOWNFILE/%s"%(end_file))
        run("ls -l %s" % end_dir)

def loging():
    print("fff")
    while True:
        s = os.listdir(config.AUTH_FILE)
        print('主机组'.center(60, '='))
        for i, v in enumerate(s):
            print('编号：%s    组名：%s' % (i, v))
        gr_name = input('选择组:')
        if gr_name == 'exit':
            exit()
        if gr_name == 'helps':
            print("fff")
            continue
        try:
            gr_file = s[int(gr_name)]
            lst = FileHand(gr_file)  # 实例连接
            lst.group_open()  # 打开
            while True:
                # print(info_l)
                inst = input('指令>>>:')
                if inst == 'exit':
                    exit()
                if inst == 'quit':
                    break
                if inst == 'helps':
                    print("fff")
                    continue
                if inst == "":
                    continue
                lst.inst_attr(inst)


        except ValueError as e:
            print(e)

loging()



