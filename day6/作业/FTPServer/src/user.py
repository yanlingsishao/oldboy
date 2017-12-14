#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-5 14:08
# @Author  : Jerry Wang
# @Site    : 
# @File    : conf.py
# @Software: PyCharm
import os, sys, pickle, socket, time

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)
from conf import settings
from common import show


class User(object):
    '''
    用户类
    '''

    def __init__(self, username, psd):
        self.name = username
        self.password = psd
        self.home_path = settings.user_home + "/" + self.name

    def login(self):
        '''
        用户登陆方法
        :return:
        '''
        user_dic = User.info_read(self.name)
        if user_dic.get(self.name) == self.password:
            show("登陆成功", "info")
            return True
        else:
            show("登陆失败，用户名或密码错误", "error")
            return False

    def register(self):
        '''
        用户注册方法
        :return:
        '''
        dic = {}
        dic[self.name] = self.password
        if User.info_write(self.name, dic):
            show("注册成功", "info")
            return True
        else:
            show("注册失败", "error")
            return False

    def view_file(self):
        '''
        查看当前目录下文件
        :return: 目录下文件名组成的列表
        '''
        if not os.path.exists(self.home_path):
            os.mkdir(self.home_path)
            with open("%s\空白文件" % self.home_path, "w") as f:
                f.write("空白文件")
        for root, dirs, files in os.walk(self.home_path):
            return files

    @staticmethod
    def download_file(filename, name, con):
        '''
        下载文件静态方法
        :param filename: 文件名
        :param name: 用户名
        :param con: 标志
        :return: none
        '''
        dir = os.path.join(os.path.join(os.path.join(Base_dir, "home"), name), filename)
        with open(dir, "rb") as f:
            # while True:
            data = f.read()
            a = str(len(data))
            # print(type(a))
            con.sendall(bytes(a, encoding="utf-8"))
            con.sendall(data)

    @staticmethod
    def receive(filename, name, res_length, con):
        '''
        接收文件静态方法
        :param filename: 文件名
        :param name: 用户名
        :param con: 标志
        :return: none
        '''
        dir = os.path.join(os.path.join(os.path.join(Base_dir, "home"), name), filename)
        length = 0
        f = open(dir, "wb")
        while True:
            data = con.recv(1024)
            length += len(data)
            f.write(data)
            # print(length)
            if length == int(res_length):
                show("文件下载成功", "info")
                f.flush()
                f.close()
                return True

    @staticmethod
    def info_read(name):
        '''
        读取用户数据的静态方法
        :param name: 用户名
        :return: 字典
        '''
        user_dir = os.path.join(settings.user_info, name)
        if os.path.exists(user_dir):
            with open(user_dir, "rb") as f:
                dic = pickle.load(f)
                return dic
        else:
            print("用户数据为空")

    @staticmethod
    def info_write(name, dic):
        '''
        写入用户数据的静态方法
        :param name:用户名
        :param dic:用户信息字典
        :return:True
        '''
        user_dir = os.path.join(settings.user_info, name)
        with open(user_dir, "wb") as f:
            pickle.dump(dic, f)
            return True