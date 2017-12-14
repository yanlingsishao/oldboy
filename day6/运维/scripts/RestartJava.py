#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-8 17:15
# @Author  : Jerry Wang
# @Site    : 
# @File    : RestartJava.py
# @Software: PyCharm
from fabric.api import *

env.user = 'root'#用config实现host,
env.hosts = [
    '192.168.1.95'
]
env.password = 'huazhen@123'


@task
def server():
    run('service network status',pty=False)
    run('service network restart',pty=False)
    run('service network status',pty=False)

