#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''

#1函数作用域
# def jj():
#     def kk():
#         def ll():
#             print("wangqiyuan")
#         return ll
#     return kk
# jj()()()

#2匿名函数
# func = lambda x:x+1  #lambda 形参:表达式
# print(func(22))


# name="alex"
# 函数结果
# def change_name(x):
#     return name+"_sb"
# res=change_name(name)
# print(res)
# 匿名函数结果
# f = lambda x:x+"_sb"
# print(f(name))