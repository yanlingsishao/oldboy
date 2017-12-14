#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# import re
# PP = ["BALANCECHANGE","RECHARGE","TRANSACTION","WITHDRAW"]
# i = "20170609_M20002661169_RECHARGE.txt"
# for k in PP:
#     x = re.findall(".+{}.+".format(k),i)
#     if x:
#         print(x)
#     else:
#         continue
# from mysql_conn import my_sql
# x = my_sql()
# x.mysql_exec("select * from user")
# y = x.get_chone()
# print(y)
# x.close()
x = ["43","43","fasd"]
y = "{},'{}'".format("fd","','".join(x))
print(y)