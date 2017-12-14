#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'honglongwei'

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


def start(ServiceName):
    '''
        Desc: Start GameServer
        CLI Example:
                czqstmod.py ServiceName start
    '''
    pid = srv_pidfile[ServiceName]
    cmd = srv_up[ServiceName]
    logging.info('{0} start'.format(ServiceName))
    if os.path.exists(pid):
        return R('GameServer is already running !')
    else:
        proc = Popen(cmd, shell=True)
        return G('Start GameServer is successful !')


def stop(ServiceName):
    '''
        Desc: Stop GameServer

        CLI Example:
                czqstmod.py ServiceName stop
    '''
    pid = srv_pidfile[ServiceName]
    cmd = srv_down[ServiceName]
    logging.info('{0} stop'.format(ServiceName))
    if os.path.exists(pid):
        proc = Popen(cmd, shell=True)
        return G('Stop GameServer is running...,please wait !')
    else:
        return R('GameServer is already stopped !')


def status(ServiceName):
    '''
        Desc: Check GameServer Status

        CLI Example:
                czqstmod.py ServiceName status
    '''
    cmd = 'ps -ef|grep "{0}"|grep -v grep'.format(ServiceName)
    proc = Popen(cmd, stdout=subprocess.PIPE, shell=True)
    item = proc.stdout.read().split('\n')[:-2]
    its = '\n'.join(item)
    cot = len(item)
    ret = its + '\n' + '*' * 80 + '\n' + 'The total of process is {0} !'.format(cot)
    logging.info('{0} status'.format(ServiceName))
    return G(ret)


def update(ServiceName, Pkg):
    '''
        Desc: Update GameServer

        CLI Example:
                czqstmod.py ServiceName update Pkg
    '''
    logging.info('{0} update {1}'.format(ServiceName, Pkg))
    if Pkg:
        fl = os.path.join(src_path, Pkg)
        try:
            zfile = zipfile.ZipFile(fl, 'r')
            for filename in zfile.namelist():
                zfile.extract(filename, des_path[ServiceName])
            return G('Update is successful !')
        except IOError:
            return R('The package is invalid !!!')
    else:
        return R('The package is invalid !!!')


def backup(ServiceName):
    '''
        Desc: Backup GameServer

        CLI Example:
                czqstmod.py ServiceName backup
    '''
    logging.info('{0} backup'.format(ServiceName))
    bakname = ServiceName + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    zipname = os.path.join(bdes_path, bakname)
    f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for bsrc_path in bsrc_path_lt[ServiceName]:
        bac_path = os.path.dirname(bsrc_path)
        ls_path = bac_path + '/'
        zg_path = bsrc_path.split(ls_path)[1]
        os.chdir(bac_path)
        for dirpath, dirnames, filenames in os.walk(zg_path):
            for filename in filenames:
                f.write(os.path.join(dirpath, filename))
    f.close()
    return G('Backup is successful !')


if __name__ == "__main__":
    if os.path.exists('./logs'):
        pass
    else:
        os.makedirs('./logs')
    log_ft = datetime.datetime.now().strftime('%Y-%m-%d-%H')
    user_cmd = getpass.getuser()
;
    opts = sys.argv
    #try:
    #     if opts[1] == '-d' or opts[1] == '--help':
    #         print G('start :') + R('{0}'.format(start.__doc__))
    #         print G('stop :') + R('{0}'.format(stop.__doc__))
    #         print G('status :') + R('{0}'.format(status.__doc__))
    #         print G('update :') + R('{0}'.format(update.__doc__))
    #         print G('backup :') + R('{0}'.format(backup.__doc__))
    #     elif opts[2] == 'start':
    #         print start(opts[1])
    #     elif opts[2] == 'stop':
    #         print stop(opts[1])
    #     elif opts[2] == 'status':
    #         print status(opts[1])
    #     elif opts[2] == 'backup':
    #         print backup(opts[1])
    #     elif opts[2] == 'update':
    #         print update(opts[1], opts[3])
    #     else:
    #         print R('Script Parameter Error !!!')
    # except IndexError:
    #     print R('Script Parameter Error !!!')