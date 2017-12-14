#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import socket

j = b"fsda"
j.decode(encoding="utf-8")

ip_port = ('127.0.0.1',8899)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print ('receive:',data)
    inp = input('please input:')
    sk.sendall(inp)
    if inp == 'exit':
        break

sk.close()