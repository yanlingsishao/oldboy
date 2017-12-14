#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import paramiko
import uuid


class Comm(object):
    def __init__(self):  # 初始化参数
        self.host = '192.168.1.111'
        self.port = 22
        self.username = 'root'
        self.pwd = '123456'


    def create_file(self):  # 本地创建文件
        file_name = str(uuid.uuid4())  # uuid创建一个不会重复的随机字符串作为文件名
        with open(file_name, 'w') as f_obj:
            f_obj.write('sb2')
            return file_name  # 返回文件名


    def run(self):
        self.connect()
        #self.upload()  # 执行上传
        self.rename()  # 执行重命名
        self.close()


    def connect(self):  # 用于ssh连接
        t = paramiko.Transport((self.host, self.port))
        t.connect(username=self.username, password=self.pwd)
        self.__transport = t


    def close(self):  # 用于ssh关闭
        self.__transport.close()


    def upload(self):  # 用于上传
        self.file_name = self.create_file()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(self.file_name, '/home/yangmv/%s' % self.file_name)


    def rename(self):  # 用于重命名
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        stdin, stdout, stderr = ssh.exec_command('mv /home/jj.kk /home/ssss.txt')
        result = stdout.read()
        # startcmd = Comm()
        # startcmd.run()

u = Comm()
u.run()
u.close()