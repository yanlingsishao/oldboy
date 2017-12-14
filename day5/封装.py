#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# class A:
#     __N=0
#     def __init__(self):
#         self.__X=10
#
#     def __foo(self):
#         print("from A")
#
#     def bar(self):
#         self.__foo()
#
# A().bar()


# class Teacher:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print("姓名：%s,年龄：%s"%(self.__name,self.__age))
#
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是整型')
#         self.__name=name
#         self.__age=age
#
# a1=Teacher("wangqiyuan","18")
# a1.tell_info()
# a1.set_info("wangqiyuan",19)
# a1.tell_info()



# class ATM:
#     def __card(self):
#         print('插卡')
#     def __auth(self):
#         print('用户认证')
#     def __input(self):
#         print('输入取款金额')
#     def __print_bill(self):
#         print('打印账单')
#     def __take_money(self):
#         print('取款')
#
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print_bill()
#         self.__take_money()
#
# a=ATM()
#
# a.withdraw()

#
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight /(self.height**2)
#
# P1=People("小明",65,1.7)
# print(P1.bmi)

# import math
# class Circle:
#     def __init__(self,redius):
#         if not isinstance(redius,int):
#             raise  redius
#         self.redius=redius
#
#     @property
#     def area(self):
#         return math.pi * self.redius**2
#
#     @property
#     def perimeter(self):
#         return 2*math.pi*self.redius
#
# c=Circle(10)
# print(c.redius)
# print(c.area)
# print(c.perimeter)


class Foo:
    def __init__(self,val):
        self.__NAME=val #将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)

    @name.setter
    def name(self,value):
        if not isinstance(value,str):  #在设定值之前进行类型检查
            raise TypeError('%s must be str' %value)
        self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')


f=Foo("egon")
print(f.name)


