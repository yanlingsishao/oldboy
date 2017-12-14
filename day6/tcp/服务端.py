#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-23 9:19
# @Author  : Jerry Wang
# @Site    : 
# @File    : 服务端.py
# @Software: PyCharm
from socket import *

ip_port = ("192.168.1.192",8000)
BUFSIZE=1024
tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)


tcp_server.listen(5)
print(">>>")
while True:

    conn,addr = tcp_server.accept()
    print("接到来自%s的电话"%addr[0])
    while True:
        try:

                msg=conn.recv(BUFSIZE)
                print(msg,type(msg))

                conn.send(msg.upper())
        except Exception:
            break


tcp_server.close()