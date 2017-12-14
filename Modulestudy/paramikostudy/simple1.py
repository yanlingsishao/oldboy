#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import paramiko


hostname = '10.2.16.7'
username = "hzjkit"
password = "kCl7Nj!Uv2~kw_"
paramiko.util.log_to_file("syslogin.logs")

# ssh=paramiko.SSHClient()
# # ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
# ssh.connect(hostname=hostname,username=username,password=password,port=22,allow_agent=False,look_for_keys=False)
#
# stdin,stdout,stderr=ssh.exec_command("uptime")
# # stdin.write("kCl7Nj!Uv2~kw_\n")
# # stdin.flush()
#
# data = stdout.read().splitlines()
# # print(data)
# for line in data:
#     if line:
#         print (line.decode("utf-8"))
# ssh.close()

transport = paramiko.Transport((hostname, 22))
transport.connect(username=username, password=password)
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin, stdout, stderr = ssh.exec_command('ls')
data = stdout.read().splitlines()
for line in data:
     if line:
         print (line.decode("utf-8"))
transport.close()
