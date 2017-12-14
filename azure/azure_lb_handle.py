#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年7月13日
@author: WangQiyuan

'''
import subprocess
import re

ps_path = r"F:\王琦渊运维\python\S4\azure"#powershell文件目录地址

######################负载名#########后端池名###########网口1###########网口2#############

ps_name_dic = {"rest-lb": ["install_lb.ps1", "uninstall_lb.ps1","p2p-rest-lb",
                           "p2p-rest-poollb","web-p2p-rest1","web-p2p-rest2"],
               "ser-lb":["install_lb.ps1", "uninstall_lb.ps1","p2p-ser-LB",
                          "p2p-ser-outpoll","web-p2p-ser1","web-p2p-ser2"],
               "front-lb":["install_lb.ps1", "uninstall_lb.ps1","p2p-front-LB",
                            "p2p-front-poollb","web-p2p-front1","web-p2p-front2"]}


class LbPowershell(object):
    """python调用powershell 操作负载功能
    lb_1为第一台，lb_2为第二台
    """
    def one_or_two(self,int_lb_name):
        # for i in ps_name_dic.keys():
        #     print(i)
        while True:
            #int_lb_name = input("请确认负载名称:")
            lb_name = (ps_name_dic.get(int_lb_name))[2:]
            lb_2 = lb_name[0:2]
            lb_2.append(lb_name[3])
            lb_1 = " ".join(lb_name[0:3])
            lb_2 = " ".join(lb_2)
            return [lb_1,lb_2]

    def deal_with_powershell(self,ps_name,argument):
        """处理powershell"""
        try:
            args=[r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe",
                  "-ExecutionPolicy","Unrestricted",r"{}\{}".format(ps_path,ps_name),argument]  #args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
            p=subprocess.Popen(args,stdout=subprocess.PIPE)
            dt=chr(p.stdout.read())#
            return dt
        except Exception as e:
            print (e)
        return False

    def batch_handle(self,args):
        """批处理删除,取到卸载文件名 0安装/1卸载"""
        for i in ps_name_dic.keys():
            uninstall = ps_name_dic.get(i)#获取该负载列表
            uninstall_filename = uninstall[args]
            which_lb = LbPowershell().which_one_lb()#选择第一个还是第二个
            which_host = LbPowershell().one_or_two(i)[which_lb]#选出第一个还是第二个的列表
            LbPowershell().deal_with_powershell(uninstall_filename,which_host)
        print("success")

    def batch_page(self):
        while True:
            int_batch_choose = input("安装(0),卸载(1)")
            if re.findall("\D",int_batch_choose):
                continue
            if int(int_batch_choose) == 0 or int(int_batch_choose) == 1:
                LbPowershell().batch_handle(int(int_batch_choose))
            else:
                continue

    def install_page(self):
        """安装负载页面"""
        install = LbPowershell().get_page("add")
        install_loadname = install[0]
        install_filename = install[1]
        which_lb = LbPowershell().which_one_lb()
        which_host = LbPowershell().one_or_two(install_loadname)[which_lb]
        LbPowershell().deal_with_powershell(install_filename[0],which_host)

    def uninstall_page(self):
        """卸载负载页面"""
        uninstall = LbPowershell().get_page("delete")
        uninstall_loadname = uninstall[0]
        uninstall_filename = uninstall[1]
        which_lb = LbPowershell().which_one_lb()
        which_host = LbPowershell().one_or_two(uninstall_loadname)[which_lb]
        LbPowershell().deal_with_powershell(uninstall_filename[1],which_host)

    def get_page(self,name):
        """调用页面"""
        print("负载名如下:")
        for i in ps_name_dic.keys():
            print(i)
        while True:
            load_name = input("Please enter the load name that you will {}(q退出):".format(name)).lstrip()
            if load_name == "q":
                exit()
            if load_name in ps_name_dic.keys():
                filename = ps_name_dic.get(load_name)
                return [load_name,filename]
            else:
                continue

    def which_one_lb(self):
        """"""
        while True:
            which_lb = input("确认操作那个负载【1,2】:")
            if re.findall("\D",which_lb):
                continue
            if int(which_lb) == 1 or int(which_lb) == 2:
                return int(which_lb)-1
            else:
                continue


    def login_lb(self):
        msg_overdue = '''
                1、卸载
                2、安装
                3、批量操作
                4、退出
                   '''
        dic_login= {
            "1": LbPowershell().uninstall_page,
            "2": LbPowershell().install_page,
            "3": LbPowershell().batch_page,
            "4": exit,
        }
        while True:
            print("".center(50, "*"))
            print(msg_overdue)
            choice = input("请输入您的操作：")
            if choice not in dic_login.keys(): continue
            res = dic_login[choice]()


if __name__=="__main__":
    k =  LbPowershell().login_lb()