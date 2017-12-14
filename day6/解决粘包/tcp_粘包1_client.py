#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-1 14:49
# @Author  : Jerry Wang
# @Site    : 
# @File    : tcp_粘包1_client.py
# @Software: PyCharm
from socket import *

ip_port = ("127.0.0.1",8082)
BUFSIZE=1024
tcp_client = socket(AF_INET,SOCK_STREAM)

tcp_client.connect(ip_port)
while True:

    s = input('>>: ').strip()
    if len(s) == 0: continue
    if s == "quit":break
    tcp_client.send(s.encode("utf-8"))

    #解决粘包
    length = int(tcp_client.recv(BUFSIZE).decode("utf-8"))
    tcp_client.send("ok".encode("utf-8"))
    recv_msg = tcp_client.recv(length)
    print(length)
    # recv_size = 0
    # recv_msg  = b''
    # while recv_size < length:
    #     recv_msg += tcp_client.recv(BUFSIZE)
    #     recv_size = len(recv_msg)
    print(recv_msg.decode("gbk"))


tcp_client.close()
