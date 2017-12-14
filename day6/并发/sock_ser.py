#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-25 15:33
# @Author  : Jerry Wang
# @Site    : 
# @File    : sock_ser.py
# @Software: PyCharm
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #print(self.request)   #conn
        print(self.client_address)   #addr

        while True:
            try:
                #收消息
                data = self.request.recv(1024)
                print(self.client_address,"收到客户端消息:",data)

                #发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(self.client_address,e)
                break

if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(("127.0.0.1",8085),MyServer)
    s.serve_forever()
