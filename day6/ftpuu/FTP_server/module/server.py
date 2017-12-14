#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-6 15:09
# @Author  : Jerry Wang
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import socketserver
import json
import configparser
import os
from conf import settings
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
class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while 1:
            data = self.request.recv(1024).strip()
            data=json.loads(data.decode("utf8"))
            '''
            {"action":"auth",
            "username":"yuan",
            "pwd":123}'''
            if data.get("action"):
                if hasattr(self,data.get("action")):
                    func = getattr(self,data.get("action"))
                    func(**data)
                else:
                    print("error cmd")
            else:
                print("Invalid cmd")

    def auth(self,**data):
        username = data["username"]
        password = data["password"]
        user =  self.authenticate(username,password)
        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def send_response(self,state_code):
        response = {"status_code":state_code,"status_message":STATUS_CODE[state_code]}
        self.request.sendall(json.dumps(response).encode("utf8"))

    def authenticate(self,username,password):
        cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        if username in cfg.sections():
            if cfg[username]["Password"] == password:
                self.user = username
                self.mainpath = os.path.join(settings.BASE_DIR,"home",self.user)
                print("passed authtication")
                return username

    def put(self,**data):
        print("data",data)
        file_name = data.get("file_name")
        file_size = data.get("file_size")
        target_path = data.get("target_path")

        abs_path = os.path.join(self.mainpath,target_path,file_name)
        has_recived = 0
        if os.path.exists(abs_path):
            has_filesize = os.stat(abs_path).st_size
            if has_filesize < file_size:
                #断点续传
                self.send_response(800)
                pass
            else:
                #文件完整存在
                self.send_response(801)
                return
        else:
            self.send_response(802)
            f = open(abs_path, "wb")

        while has_recived < file_size:
            data = self.request.recv(1024)
            f.write(data)
            has_recived+=len(data)

        f.close()