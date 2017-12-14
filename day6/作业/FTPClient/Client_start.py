#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-5 14:06
# @Author  : Jerry Wang
# @Site    : 
# @File    : Client_start.py
# @Software: PyCharm
import socket, os, sys, time

Basedir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "FTPServer")
updir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "示例文件夹")
sys.path.append(Basedir)
from conf import settings


def upload(client, user_info, name):
    '''
    客户端上传文件的函数
    :param client:scoket客户端标志
    :param user_info:客户端登陆用户的信息
    :param name:客户端登陆用户的名字
    :return:none
    '''
    print("\033[1;37m当前可选上传\033[0m".center(40, "*"))
    dic = {}
    for root, dirs, files in os.walk(updir):
        for i, j in enumerate(files):
            k = i + 1
            dic[k] = j
            print("\033[1;37m%s：%s\033[0m" % (k, j))
    choice = input("请输入要上传的文件序号：>>>")
    command = "UPFILE+" + user_info + "+" + dic[int(choice)]
    client.sendall(bytes(command, encoding="utf-8"))
    res = client.recv(1024)
    if str(res, encoding="utf-8") == "True":
        dir = os.path.join(updir, dic[int(choice)])
        with open(dir, "rb") as f:
            data = f.read()
            a = str(len(data))
            client.sendall(bytes(a, encoding="utf-8"))
            client.sendall(data)
            time.sleep(0.5)
            print("\033[1;37m文件上传成功\033[0m")


def download(client, user_info, name):
    '''
    客户端下载文件的函数
    :param client: scoket客户端标志
    :param user_info: 客户端登陆的用户信息
    :param name:客户端登陆的用户名字
    :return: none
    '''
    dic = {}
    command = "download+" + user_info
    client.sendall(bytes(command, encoding="utf-8"))
    data = client.recv(4069)
    res = eval(str(data, encoding="utf-8"))
    if len(res) == 0:
        print("\033[1;31m当前目录下暂无文件\033[0m".center(40, "-"))
    else:
        for i, j in enumerate(res):
            k = i + 1
            dic[k] = j
            print("\033[1;37m%s：%s\033[0m" % (k, j))
        choice = input("请选择要下载的文件序号：>>>")
        cm = "downloadfile+" + dic[int(choice)] + "+" + name
        client.sendall(bytes(cm, encoding="utf-8"))
        print("\033[1;37m准备开始下载文件\033[0m")
        dir = os.path.join(updir, dic[int(choice)])
        res_length = str(client.recv(1024).decode())
        length = 0
        with open(dir, "wb") as f:
            while True:
                data = client.recv(1024)
                length += len(data)
                f.write(data)
                if length >= int(res_length):
                    print("\033[1;37m文件下载成功\033[0m")
                    time.sleep(0.5)
                    break


def view_file(client, user_info, name):
    '''
    客户端查看当前目录下文件的函数
    :param client: scoket客户端标志
    :param user_info: 客户端登陆的用户信息
    :param name: 客户端登陆的用户名字
    :return: none
    '''
    command = "view+" + user_info
    client.sendall(bytes(command, encoding="utf-8"))
    data = client.recv(1024)
    res = eval(str(data, encoding="utf-8"))
    if len(res) == 0:
        print("\033[1;31m当前目录下暂无文件\033[0m".center(40, "-"))
    else:
        for i in res:
            print("\033[1;35m%s\033[0m" % i)


def operate(client, user_info, name):
    '''
    客户端操作主函数
    :param client: scoket客户端标志
    :param user_info: 客户端登陆的用户信息
    :param name: 客户端登陆的用户名字
    :return: none
    '''
    dic = {"1": upload, "2": download, "3": view_file}
    info = '''------操作指令------
    1、上传文件
    2、下载文件
    3、查看目录下文件
    4、退出
    '''
    while True:
        print("\033[1;33m%s\033[0m" % info)
        choice = input("请输入你要操作的命令：>>>").strip()
        if choice.isdigit() and 0 < int(choice) <= len(dic):
            dic.get(choice)(client, user_info, name)
        elif int(choice) == 4:
            break
        else:
            print("\033[1;31m输出错误\033[0m".center(40, "-"))


def com_parse(client, com):
    '''
    客户端用户登陆注册命中解析函数
    :param client: 客户端scoket标志
    :param com: 命令
    :return: 登陆成功返回True，否则False
    '''
    # print(com)
    client.sendall(bytes(com, encoding="utf-8"))
    re = client.recv(4096)
    if str(re, encoding="utf-8") == "Success":
        return True
    elif str(re, encoding="utf-8") == "Success":
        return False


def login(client, data):
    '''
    客户端用户登陆函数
    :param client: 客户端scoket标志
    :param data: 数据
    :return: none
    '''
    name = input("请输入您的名字：>>>").strip()
    psd = input("请输入密码：>>>").strip()
    user_info = name + "+" + psd
    com = "login+" + user_info
    if com_parse(client, com):
        operate(client, user_info, name)
    else:
        print("\033[1;31m登陆出现异常\033[0m")


def register(client, data):
    '''
    客户端用户注册函数
    :param client: 客户端scoket标志
    :param data: 数据
    :return: none
    '''
    name = input("请输入您的名字：>>>").strip()
    psd = input("请输入密码：>>>").strip()
    com = "register+" + name + "+" + psd
    if com_parse(client, com):
        user_info = name + "+" + psd
        print("\033[1;31m注册成功\033[0m")
        command = "view+" + user_info
        client.sendall(bytes(command, encoding="utf-8"))
        res1 = client.recv(1024)
        operate(client, user_info, name)
    else:
        print("\033[1;31m注册出现异常\033[0m")


def quit(client, data):
    '''
    程序退出函数
    :param client: 客户端scoket标志
    :param data: 用户数据
    :return: none
    '''
    exit()


def main_func(client, data):
    '''
    客户端主菜单函数
    :param client: 客户端scoket标志
    :param data: 数据
    :return: none
    '''
    dic = {"1": login, "2": register, "3": quit}
    info = '''------用户登录界面------*{0}*
        1、登陆
        2、注册
        3、退出
    '''.format(str(data, encoding="utf-8"))
    print("\033[1;33m%s\033[0m" % info)
    what = input("你要干嘛？>>>").strip()
    if what.isdigit() and 0 < int(what) <= len(dic):
        dic.get(what)(client, data)
    else:
        print("\033[1;31m输出错误\033[0m".center(40, "-"))


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", settings.PORT))
    main_func(client, client.recv(1024))
    client.close()