#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-8 17:11
# @Author  : Jerry Wang
# @Site    : 
# @File    : ExecCmd.py
# @Software: PyCharm
# local,执行本地命令,如local('uname -s')
# lcd,切换本地目录,如lcd('/home')
# cd,切换远程目录
# run,执行远程命令
# sudo,sudo方式执行远程命令
# put,上传文件到远程主机 put('/home/aaa','/home/xby/aaa')
# get,从远程主机下载文件到本地 get('/opt/bbb','/home/bbb')
# prompt,获取用户输入
# confirm，获得提示信息确认,如confirm('Continue[Y/N]?')
# reboot,重启远程主机，如reboot()
# @task函数装饰器，标识函数为fab可调用的，否则对fab不可见
# @runs_once,标识函数只会执行一次，不受多台主机影响。
# @roles,表示函数执行时的主机角色
# @parallel(pool_size=)
# @with_settings()

# fabric.contrib.console.confirm(question, default=True) 用户输入Y/n,返回True/False
from fabric.api import *
env.hosts = ["192.168.1.95"]
env.user = "root"
env.password = "huazhen@123"

def cmd(args):
    '''
    fab - f ExecCmd.py cmd:args = ifconfig
    '''
    return run(args)

#
# @runs_once
# def input_raw():
#     return prompt("please input dir name:",default='/home')
#
# def worktask(dirname):
#     run("ls -l "+dirname)
#
# #@task
# def go():
#     while 1:
#         dirname=input_raw()
#         worktask(dirname)
#         if dirname:
#             while 1:
#                 cmd_input = prompt("%s out:"%env.hosts)
#                 if cmd_input == "":
#                     break
#                 local('fab -f ExecCmd.py cmd:args="%s"'%cmd_input)
#         else:
#             continue

# import subprocess
# sub=subprocess.call("fab -f ExecCmd.py cmd:args=ifconfig",shell=True,stdout=subprocess.PIPE)
# print(sub.stdout.read())
import os
os.system("fab -f ExecCmd.py cmd:args=ifconfig")
