#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# import paramiko
# #创建ssh对象
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.1.53', port=22, username='root', password='huazhen@123')
# stdin, stdout, stderr = ssh.exec_command('df')
# result = stdout.read()
# print(result)
# ssh.close()

import random
res=random.random()
print(res)



