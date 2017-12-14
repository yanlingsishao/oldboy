#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-6 14:12
# @Author  : Jerry Wang
# @Site    : 
# @File    : FTP_client.py
# @Software: PyCharm
import socket
import optparse
import json
import os
import configparser
STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'fabfile.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",

    800 : "the file exist,but not enough ,is continue? ",
    801 : "the file exist !",
    802 : " ready to receive datas",

    900 : "md5 valdate success"

}
class ClientHandler():

    def __init__(self):
        self.op = optparse.OptionParser()
        self.op.add_option("-s","--server",dest="server")
        self.op.add_option("-P", "--port", dest="port")
        self.op.add_option("-u", "--username", dest="username")
        self.op.add_option("-p", "--password", dest="password")
        self.options,self.args = self.op.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()
        self.mainpath = os.path.dirname(os.path.abspath(__file__))

    def verify_args(self,options,args):
        server = options.server
        port = options.port
        username = options.username
        password = options.password
        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit("the port is in 0-65535")

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,int(self.options.port)))

    def interactive(self):
        if self.authenticate():
            print("begin to interactive")
            cmd_info = input("{%s}"%self.user).strip()
            cmd_list = cmd_info.split()
            if hasattr(self,cmd_list[0]):
                func = getattr(self,cmd_list[0])
                func(*cmd_list)

    def put(self,*cmd_list):
        action,local_path,target_path = cmd_list
        local_path = os.path.join(self.mainpath,local_path)
        file_name = os.path.basename(local_path)
        file_size = os.stat(local_path).st_size
        data = {
            "action":"put",
            "file_name":file_name,
            "file_size":file_size,
            "target_path":target_path
        }
        has_sent = 0
        self.sock.send(json.dumps(data).encode("utf8"))
        is_exist = self.sock.recv(1024).decode("utf8")
        if is_exist == "800":
            pass

        elif is_exist == "801":
            return

        else:
            pass

        while has_sent < file_size:
            f = open(local_path,"rb")
            f.read(1024)


    def authenticate(self):

        if self.options.username is None or self.options.password is None:
            username = input("username: ")
            password = input("password: ")
            return self.get_auth_result(username,password)
        return self.get_auth_result(self.options.username,self.options.password)

    def get_auth_result(self,user,pwd):
        data = {
            "action":"auth",
            "username":user,
            "password":pwd
        }
        self.sock.send(json.dumps(data).encode("utf8"))
        data = self.response()
        #print(data["status_code"])
        if data["status_code"] == 254:
            self.user =user
            print(STATUS_CODE[254])
            return True
        else:
            print(STATUS_CODE[data["status_code"]])

    def response(self):
        data = self.sock.recv(1024).decode("utf8")
        data = json.loads(data)
        return data


ch = ClientHandler()
ch.interactive()