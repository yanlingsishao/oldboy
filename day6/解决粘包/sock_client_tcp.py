#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-23 15:59
# @Author  : Jerry Wang
# @Site    : 
# @File    : sock_client_tcp.py
# @Software: PyCharm
from socket import *

ip_port = ("127.0.0.1",8089)
BUFSIZE=1024
tcp_client = socket(AF_INET,SOCK_STREAM)

tcp_client.connect(ip_port)
while True:
    s = input('>>: ').strip()
    if len(s) == 0: continue
    if s == "quit":break

    tcp_client.send(s.encode("utf-8"))
    msg=tcp_client.recv(BUFSIZE)
    print(msg.decode("gbk"))


tcp_client.close()