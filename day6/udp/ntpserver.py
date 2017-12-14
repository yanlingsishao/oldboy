#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-23 15:36
# @Author  : Jerry Wang
# @Site    : 
# @File    : udp实现ntpserver.py
# @Software: PyCharm
import time
import socket
ip_port=('127.0.0.1',9001)
BUFSIZE=1024
udp_server_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_server_client.bind(ip_port)

while True:
    msg,addr=udp_server_client.recvfrom(BUFSIZE)
    if not msg:
        msg = "%Y-%m-%d %X"
    else:
        msg = msg.decode("utf-8")
    back_time = time.strftime(msg)
    udp_server_client.sendto(back_time.encode("utf-8"),addr)