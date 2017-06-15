#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月10日
@author: WangQiyuan
'''
# 三次机会重试
n = 0
real_user = 'wangqiyuan'
real_passwd = 123
h = open('user_lock','r')
lock_file = h.read()
h.close()
user = input("please input your user:")

for i in range(1):
    if lock_file == real_user:
        print("抱歉，您的账号已被锁定")
        exit()
    else:
        continue

while True:
    if user != 'wangqiyuan':
        print("无此用户，请重新输入")
        user = input("please input your user:")
        continue
    passwd = input("please input your passwd:")
    if n > 2:
        print("对不起，您输入的账号已超出限制，将要锁定您的账号")
        h = open('user_lock', 'w')
        h.write('%s' % user)
        h.close()
        break

    if user == 'wangqiyuan' and passwd == '123':
        print("欢迎登录")
        print('........')
        break
    else:
        print("密码错误，请重新输入")
        n += 1






