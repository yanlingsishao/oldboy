#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import paramiko
hostname = '192.168.1.111'
username = "root"
password = "123456"
paramiko.util.log_to_file("syslogin.log")

ssh=paramiko.SSHClient()
# ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect(hostname=hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
stdin,stdout,stderr=ssh.exec_command("free -m")
print(stdout.read())
ssh.close()