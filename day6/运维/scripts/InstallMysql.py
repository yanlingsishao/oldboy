#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-8 17:12
# @Author  : Jerry Wang
# @Site    : 
# @File    : InstallMysql.py
# @Software: PyCharm
import os
import sys
import re

base_dir = '/opt/software/mysql-5.7.17-linux-glibc2.5-x86_64'

os.chdir('/opt/software')
tar_result = os.system('tar xvf %s &>/dev/null' % sys.argv[1])
if tar_result == 0:
    os.chdir('/usr/local')
    os.system('ln -s %s  mysql' % base_dir)
else:
    print "uncompress wrong"

user_result = os.system('id mysql')
if user_result==0:
    print "user exist"
else:
    os.system('groupadd mysql')
    os.system('useradd -g mysql -M -s /sbin/login mysql')

os.system('mkdir -p /data/mysql/mysql3306/{data,logs,tmp}')
os.system('chown -R mysql:mysql /data/mysql/mysql3306/')
os.system('chown -R mysql:mysql /opt/software/mysql-5.7.17-linux-glibc2.5-x86_64')
os.system('chown -R mysql:mysql /usr/local/mysql')
os.chdir('/opt/software')
os.system('cp my.cnf /etc/my.cnf')
os.chdir('/usr/local/mysql')
init = os.system('./bin/mysqld --initialize')
if init == 0:
    with open('/data/mysql/mysql3306/data/error.log') as fobj:
        for line in fobj:
            if 'root@localhost' in line:
                m = re.search('(root@localhost:)(.+)',line)
                if m:
                    passwd = m.group(2)
                    print "password:%s" % passwd
os.system('cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld')
os.system('export PATH=$PATH:/usr/local/mysql/bin')
with open('/etc/profile','a+') as profile:
    profile.write('\nPATH=$PATH:/usr/local/mysql/bin')