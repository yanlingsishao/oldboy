#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-25 15:36
# @Author  : Jerry Wang
# @Site    : 
# @File    : sock_cli.py
# @Software: PyCharm
from socket import *

ip_port = ("127.0.0.1",8085)
BUFSIZE=1024
tcp_client = socket(AF_INET,SOCK_STREAM)

tcp_client.connect_ex(ip_port)
while True:

    s = input('>>: ').strip()
    if len(s) == 0: continue
    tcp_client.send(s.encode("utf-8"))


    msg=tcp_client.recv(BUFSIZE)

    print(msg.decode("utf-8"))


tcp_client.close()