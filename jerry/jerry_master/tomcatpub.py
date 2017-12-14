#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
__author__ = 'honglongwei'
import paramiko

import os
import sys
import time
import zipfile
import datetime
import getpass
import logging
import subprocess
from subprocess import Popen


# src update package path
src_path = '/home/mrdTomcat/update'#更新的包

# des update package path
des_path = {'frontweb': '/usr/local/tomcat1/wwebapps',
            'backweb': '/usr/local/tomcat/webapps',
            'restweb': '/usr/local/tomcat/webapps',
            'h5web': '/usr/local/tomcat/webapps',
            }

bsrc_path_lt = {'tomcat': ['/tmp/2', '/tmp/1'],
                'apache': ['/usr/local/apache2/conf'],
                'websocket': ['/tmp']}

# des backup package path
bdes_path = '/home/mrdTomcat/version_bak'

# service name and server start bin
srv_up = {'frontweb': '/usr/local/tomcat/bin/startup.sh',
            'backweb': '/usr/local/tomcat/bin/startup.sh',
            'restweb': '/usr/local/tomcat/bin/startup.sh',
            'h5web': '/usr/local/tomcat/bin/startup.sh',
           }


# service name and server stop bin
srv_down = {'frontweb': '/usr/local/tomcat/bin/shutdown.sh',
            'backweb': '/usr/local/tomcat/bin/shutdown.sh',
            'restweb': '/usr/local/tomcat/bin/shutdown.sh',
            'h5web': '/usr/local/tomcat/bin/shutdown.sh',
            }

# server pidfile path
srv_pidfile = {'frontweb': '/usr/local/tomcat/pid/tomcat.pid',
                'backweb': '/usr/local/tomcat/pid/tomcat.pid',
                'restweb': '/usr/local/tomcat/pid/tomcat.pid',
                'h5web': '/usr/local/tomcat/pid/tomcat.pid'}


# change return color
def G(s):#绿色
    return "%s[32;2m%s%s[0m" % (chr(27), s, chr(27))


def A(s):#淡绿色
    return "%s[36;2m%s%s[0m" % (chr(27), s, chr(27))

def R(s):#红色
    return "%s[31;2m%s%s[0m" % (chr(27), s, chr(27))

class TomcatPub(object):
    def __init__(self,host,user,passwd,port=22):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.port=port

    def conn_ssh(self,command):
        self.transport = paramiko.Transport(self.host,self.port)
        self.transport.connect(username=self.user, password=self.passwd)
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(command)
        res=stdout.read()
        return res

    def close(self):
        self.transport.close()

    # def save_pidfile(self):
    #     with


    # def start_tom(self):
    #     '''start tomcat service'''
    #     pid = srv_pidfile[self.serviceName]
    #     cmd = srv_down[self.serviceName]
    #     logging.info('{0} stop'.format(self.serviceName))
    #     if os.path.exists(pid):
    #         proc = Popen(cmd, shell=True)
    #         return G('Stop GameServer is running...,please wait !')
    #     else:
    #         return R('GameServer is already stopped !')


x = TomcatPub("192.168.1.93","root","huazhen@123")
y = x.conn_ssh("ps -ef | grep tomcat | grep -v grep | awk '{print $2}'")

x.close()