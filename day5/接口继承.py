#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import abc


#接口继承


class Interface(metaclass=abc.ABCMeta):#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
    @abc.abstractclassmethod
    def read(self): #定接口函数read
        pass
    @abc.abstractclassmethod
    def write(self): #定义接口函数write
        pass


class Txt(Interface): #文本，具体实现read和write
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(Interface): #磁盘，具体实现read和write
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(Interface):
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的写入方法')



m1 = Process()
m1.write()

