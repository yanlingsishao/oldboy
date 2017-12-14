#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import time
time.sleep(30)
class Foo:
    x = 1
    def __init__(self,y):
        self.y = y

    def __getattr__(self, item):
        print("----> from getattr:你的属性不存在")

    def __setattr__(self, key, value):
        print("--->from setattr")

    def __delattr__(self, item):
        print("--->from delattr")
        self.__dict__.pop(item)

# __setattr__添加/修改属性会触发它的执行
f1 = Foo(10)
print(f1.__dict__)

f1.z = 3
print(f1.__dict__)

#__delattr__删除属性的时候会触发
# f1=Foo(10)
# f1.__dict__["a"]=3
# del f1.a
# print(f1.__dict__)

#
f1=Foo(10)
f1.xxxxxxx



