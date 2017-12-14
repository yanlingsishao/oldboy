#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-23 15:36
# @Author  : Jerry Wang
# @Site    : 
# @File    : udp实现ntpclient.py
# @Software: PyCharm
import socket
ip_port=('127.0.0.1',9001)
BUFSIZE=1024
udp_server_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    # if not msg:continue

    udp_server_client.sendto(msg.encode('utf-8'),ip_port)

    back_msg,addr=udp_server_client.recvfrom(BUFSIZE)
    print("服务端的时间:{}".format(back_msg.decode('utf-8')))