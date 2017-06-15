#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# op = open("xxx","w",encoding="utf-8")
# tt = op.writelines(["gfase\n","dfa\n"])
# op.close()

# with open("xxx","w",encoding="utf-8") as tt,\
#     open("xxxx","w",encoding="utf-8") as yy:
#     tt.write("fasdfadsf")
#     yy.write("fasdfasdfasdfasdf")

f=open("xxx","r",newline="")
# data=f.read()
# print(data)
# print(data.decode("utf-8"))


print(f.tell())#光标所在的位置
print(f.readlines())
print(f.tell())

