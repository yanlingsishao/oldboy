#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年7月25日
@author: WangQiyuan

'''
from ftplib import FTP
import re
import os

class myFtp(object):
    ftp = FTP()
    def __init__(self,host,port=21):
        self.ftp.connect(host,port)# 连接的ftp sever和端口

    def login(self,user,passwd):
        '''登录'''
        self.ftp.login(user,passwd)# 连接的用户名，密码
        self.ftp.cwd("2017")

    def ftp_gets(self):
        '''目录结构放入字典'''
        files_dics = {}
        files_list=[]
        dirs_list = self.ftp.nlst()#目录结构放进列表
        mouth_num=len(dirs_list)
        for i in range(mouth_num):
            dir_name = dirs_list[i]
            self.ftp.cwd(dir_name)
            files_dics.update({dir_name:self.ftp.nlst()})
            self.ftp.cwd("../")
        return files_dics



    def downloadfile(self,mouth,filename):
        '''下载单文件'''
        x = os.path.exists("F:\\王琦渊运维\\python\\S4\\ftpindb\\data\\{}".format(mouth))
        if x == False:
            os.mkdir(r"F:\\王琦渊运维\\python\\S4\\ftpindb\\data\\{}".format(mouth))
        localpath = r"F:\\王琦渊运维\\python\\S4\\ftpindb\\data\\{}\\{}".format(mouth,filename)
        bufsize = 1024
        filepath = "/2017/{}/{}".format(mouth,filename)
        fp=open(localpath,"wb")
        self.ftp.retrbinary('RETR {}'.format(filepath),fp.write,bufsize)
        fp.close()                         # 接收服务器上文件并写入本地文件

    def detection(self,kwargs):
        '''验证为后缀为ok的文件'''
        true_dics={}
        list_file= list(kwargs.keys())
        for i in range(len(list_file)):
            true_list = []
            list_files = kwargs.get(list_file[i])
            for x in list_files:
                if  x.endswith(".ok") == True:
                    str_filename="".join(re.findall("\w+\.",x))
                    true_list.append("{}txt".format(str_filename))
                    true_dics.update({list_file[i]: true_list})
                else:
                    continue
        return true_dics

    def close(self):
        self.ftp.quit()


def batch_down():
    '''批量下载'''
    ftp_conn = myFtp("oYJKnkwaNRyxIiQ.unitedbank.cn")
    ftp_conn.login("M20002661169", "TNcSkrUC")
    file_dic = ftp_conn.ftp_gets()#获取所有的dic
    true_dic = ftp_conn.detection(file_dic)#获取有ok的dic
    list_file = list(true_dic.keys())  # 获取月路径
    for i in range(len(list_file)):
        mouth = list_file[i]  # 月
        file_name_list = true_dic.get(mouth)  # 获取文件列表
        for x in file_name_list:
            ftp_conn.downloadfile(mouth,x)
    ftp_conn.close()

if __name__ == "__main__":
    batch_down()


