#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
#
# class X:
#     def __format__(self, format_spec):
#     def __slots__(self):

class Foo:
    __slots__=['name','age']

f1=Foo()
f1.name='alex'
f1.age=18
print(f1.__slots__)

f2=Foo()
f2.name='egon'
f2.age=19
print(f2.__slots__)

print(Foo.__dict__)