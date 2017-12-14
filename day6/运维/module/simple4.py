#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-11 16:18
# @Author  : Jerry Wang
# @Site    : 
# @File    : simple4.py
# @Software: PyCharm

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
import os,sys
front = os.path.abspath("../file/UPFILE/FRONT_TAR/p2p.war")
h5 = os.path.abspath("../file/UPFILE/SERVICE_TAR/p2p-h5.war")

class Simple:
    env.user = "hzjkit"
    env.hosts = ["10.2.16.8","10.2.16.19"]
    env.passwords = {"hzjkit@10.2.16.8":"v6Qn=!|9t9#rqxu/~d7l",
                     "hzjkit@10.2.16.19":"l!VBN`xmde;5$1'dgU@7",}
    # def __init__(self,env.user,hosts,password):
    #     self.user = env.user
    #     self.hosts = env.hosts
    #     self.password = env.password

    #@task
    def put_task(self):
        sudo("mkdir -p /data")
        with cd("/data"):
            with settings(warn_only=True):
                result = put(front,"/data")
            if result.failed and not confirm("put file faild,Continue[Y/N]?"):
                abort("Aborting file put task!")


def run():
    front3 = Simple(user="hzjkit",hosts=["10.2.16.8"],password="v6Qn=!|9t9#rqxu/~d7l")
    front3.put_task()
