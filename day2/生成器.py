#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月31日
@author: WangQiyuan

'''
# laomuji=('鸡蛋%s' %i for i in range(10))#生成器表达式
# print(laomuji)
# print(next(laomuji)) #next本质就是调用__next__
# print(laomuji.__next__())
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
# print(next(laomuji))
#
# print(sum(x ** 2 for x in range(10000000)))

# import time
# def diedai():
#     print("我出生了")
#     yield "我"
#     time.sleep(2)
#     print("开始生儿子了")
#     yield "儿子"
#     time.sleep(2)
#     print("开始生孙子了")
#     yield "孙子"
# res = diedai()
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# import time
# def product_baozi():
#     for i in range(10000):
#         print("大师正在生产包子")
#         yield "包子%s"%i


# pro_g=product_baozi()
# baozil=pro_g.__next__()
# print("来了一个人，吃包子",baozil)
# baozil1=pro_g.__next__()
# print("来了一个人，吃包子",baozil1)
# def xiaofei():
#     for x in range(10):
#         print("小%s来了,想要吃包子"%x)
#         x = pro_g.__next__()
#         print("小%s吃包子"%x, x)
# pro_g=product_baozi()
# xiaofei()


# def lay_eggs(num):
#     for egg in range(num):
#         res='蛋%s' %egg
#         yield res
#         print('下完一个蛋')
#
# laomuji=lay_eggs(10)#我们拿到的是一只母鸡
# print(laomuji)
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(laomuji.__next__())

x = open("jj","r",encoding="utf-8")
y = x.readlines()
res="sb" if "sb" in y else print("false")