#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-23 15:59
# @Author  : Jerry Wang
# @Site    : 
# @File    : socket_server_tcp.py
# @Software: PyCharm

from socket import *
import subprocess
import socketserver

ip_port = ("127.0.0.1",8082)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("新的客户端连接",self.client_address)
        while True:
            try:
                cmd = self.request.recv(buffer_size)
                if not cmd:break
                print("收到客户端的命令",cmd.decode("utf-8"))
                res = subprocess.Popen(cmd.decode("utf-8"),shell=True,
                                       stderr=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
                err = res.stderr.read()
                if err:
                    cmd_res = err
                else:
                    cmd_res = res.stdout.read()
                if not cmd_res:
                    cmd_res ='执行成功'.encode("gbk")
                length = len(cmd_res)

                self.request.send(cmd_res)

            except Exception as e:
                break




if __name__ == "__main__":
    '基于线程'
    s = socketserver.ThreadingTCPServer(("127.0.0.1",8089),MyServer)
    s.serve_forever()