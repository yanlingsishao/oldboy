#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-5 14:08
# @Author  : Jerry Wang
# @Site    : 
# @File    : Server_start.py
# @Software: PyCharm
import socket, os, sys

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)
from conf import settings
from common import show
from user import User


def fuck_tcp(con, addr):
    '''
    服务端数据解析主函数
    :param con:
    :param addr:
    :return:
    '''
    show("收到{0}的连接请求，正在通信中。。。".format(addr), "info")
    con.sendall(bytes("连接成功", encoding="utf-8"))
    while True:
        cmd = con.recv(4096)
        if not cmd:
            break
        else:
            # try:
            data = str(cmd.decode(encoding="utf-8"))
            res = data.split("+")
            if res[0] == "login":
                show("收到客户端登陆的请求，正在登陆。。。", "msg")
                name = res[1]
                psd = res[2]
                user = User(name, psd)
                sign = user.login()
                if sign:
                    con.sendall(bytes("Success", encoding="utf-8"))
                else:
                    con.sendall(bytes("Failure", encoding="utf-8"))
            elif res[0] == "register":
                show("收到客户端注册的请求，正在注册。。。", "msg")
                name = res[1]
                psd = res[2]
                user = User(name, psd)
                if user.register():
                    con.sendall(bytes("Success", encoding="utf-8"))
                else:
                    con.sendall(bytes("Failure", encoding="utf-8"))
            elif res[0] == "view":
                show("收到客户端创建或查看当前目录文件的请求。。。", "msg")
                name = res[1]
                psd = res[2]
                user = User(name, psd)
                res = user.view_file()
                file = str(res)
                con.sendall(bytes(file, encoding="utf-8"))
                show("当前目录文件查看或创建成功", "info")
            elif res[0] == "UPFILE":
                show("收到客户端上传文件的请求。。。", "msg")
                name = res[1]
                filename = res[3]
                con.sendall(bytes("True", encoding="utf-8"))
                res_length = str(con.recv(1024).decode())
                User.receive(filename, name, res_length, con)
            elif res[0] == "download":
                show("收到客户端下载文件的请求。。。", "msg")
                name = res[1]
                psd = res[2]
                user = User(name, psd)
                res = user.view_file()
                file = str(res)
                con.sendall(bytes(file, encoding="utf-8"))
            elif res[0] == "downloadfile":
                show("开始下载文件", "msg")
                User.download_file(res[1], res[2], con)
                show("文件下载成功", "info")


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", settings.PORT))
    server.listen(5)
    show("正在监听[%s]地址[%s]端口，等待连接。。。" % (settings.HOST, settings.PORT), "info")
    con, addr = server.accept()
    fuck_tcp(con, addr)