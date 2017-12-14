#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# class Dad:
#     money = 100
#     def __init__(self,name):
#         print("爸爸")
#         self.name = name
#
#     def hit_son(self):
#         print("%s正在打儿子"%self.name)
#
# class Son(Dad):
#     def __init__(self,name,age):
#         print("儿子")
#         self.name = name
#         self.age = age
#
#     def hit_son(self):
#         print("来自儿子类")
#
#
#
#

class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar(Foo):
    def f1(self):
        print('Foo.f11')

b = Bar()
b.f2()







# s1 = Dad("大明")
# print(s1.name)
# print(s1.money)
# s1.hit_son()


# c1 = Son("小明",19)
# print(c1.name)
# print(c1.money)
# c1.hit_son()