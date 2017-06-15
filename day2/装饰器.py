#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# 高阶函数 函数嵌套 闭包
#
# 高阶函数定义
# 1.函数接收的参数是一个函数名
# 2.函数的返回值是一个函数名
# 3.满足上述条件任意一个,都可称之为高阶函数
# (1)
# import time
# def foo():
#     time.sleep(3)
#     print("hell，你好")
# def test(func):
#     start_time=time.time()
#     func()
#     stop_time=time.time()
#     print("函数运行时间是%s"%(stop_time-start_time))
#
# test(foo)
# (2)
# def foo():
#     print("nihao")
# def test(func):
#     return func
# # res=test(foo)
# # res()
# foo=test(foo)
# foo()
# (3)不修改foo源代码，不修改foo调用方式
# import time
# def foo():
#     time.sleep(3)
#     print("nihao")
# def test(func):
#     return func
# def timer(func):
#     start_time = time.time()
#     func()
#     stop_time=time.time()
#     print("函数运行时间是%s"%(stop_time-start_time))
#     return func
# foo=timer(foo)
#
# 函数嵌套
# def father(name):
#     print('from father %s' %name)
#     def son():
#
#         print('from son')
#         def grandson():
#             print('from grandson')
#         grandson()
#     son()
#
# father('王琦渊')
#
# 闭包，作用域的一种体现
#
#装饰器实现，有返回值的
import time
def timer(func):
    def wraper():
        start_time=time.time()
        res=func()#就是在运行test()
        stop_time=time.time()
        print("运行时间是%s"%(stop_time-start_time))
        return res
    return wraper

@timer# 相当于test=timer(test)#返回的是wraper的内存地址
def test():
    time.sleep(3)
    return "这是test的返回值"

res=test()#就是在运行wrapper
print(res)#wrapper的返回值

# 装饰器实现，加参数的
# import time
# def timer(func):
#     def wraper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)#就是在运行test()
#         stop_time=time.time()
#         print("运行时间是%s"%(stop_time-start_time))
#         return res
#     return wraper
# @timer# 相当于test=timer(test)#返回的是wraper的内存地址，所有修改wraper就达到加参数的作用
# def test(name,age):
#     time.sleep(3)
#     print("test函数运行完毕,名字是%s，年龄是%d"%(name,age))
#     return "这是test的返回值"
# @timer
# def test1(name,age,gender):
#     time.sleep(3)
#     print("test1函数运行完毕,名字是%s，年龄是%d,性别是%s"%(name,age,gender))
#     return "这是test1的返回值"
#
# res=test("wangqiyuan",18)#就是在运行wrapper
# res=test1("wangqiyuan",18,"man")
# print(res)#wrapper的返回值
#
# 解压补充
# l=[10,12,15,1,12,20,15,35,0,1,5]
#
# a,b,*_,c=l
# print(a)
# print(b)
# print(c)
#
# n1=1
# n2=2
# print(n1,n2)
# n1,n2=n2,n1
# print(n1,n2)