#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-8 16:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : fabfile.py
# @Software: PyCharm

from fabric.api import run,env

env.hosts = ["root@192.168.1.95:22"]
env.user = "root"
env.password = "huazhen@123"

def command():
    run("ls")





