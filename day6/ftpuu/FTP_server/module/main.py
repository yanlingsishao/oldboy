#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-6 14:13
# @Author  : Jerry Wang
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import optparse
import socketserver
from conf import settings
from module import server
class ArgvHandler():
    def __init__(self):
        self.op = optparse.OptionParser()
        # self.op.add_option("-s","--server",dest="server")
        # self.op.add_option("-P","--port",dest="port")
        option,args = self.op.parse_args()
        self.verify_args(option,args)
        # print(option)
        # print(args)

    def verify_args(self,option,args):
        cmd = args[0]
        if hasattr(self,cmd):#反射常用
            foo = getattr(self,cmd)
            foo()

    def start(self):
        print("start ok")
        s = socketserver.ThreadingTCPServer((settings.IP,settings.PORT),server.ServerHandler)
        s.serve_forever()













