#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''


class Vehicle:
    Country='China'
    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power

    def run(self):
        print("开动了")

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)
        self.line=line

    def run(self):
        print("地铁%s号线欢迎您" %self.line)
        Vehicle.run(self)

line13=Subway("中国地铁","1000m/s","1000人/每箱","电",13)

line13.run()

