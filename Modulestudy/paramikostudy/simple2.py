#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import paramiko
t = paramiko.Transport(("192.168.1.111",22))
t.connect(username="root",password="123456")
sftp = paramiko.SFTPClient.from_transport(t)

localpath=r"F:\新建文件夹\host"
remotepath="/home/jj.ll"

# sftp.put(localpath,remotepath)#发
# sftp.get(remotepath,localpath)#收
# sftp.stat(remotepath)#获取sftp服务器端指定文件信息
# sftp.mkdir("/home/userdir",0755)