#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年8月31日
@author: WangQiyuan

'''
# '''经典类实现多继承
# ---A查找-无-----B查找--无----D查找--无-----C查找--无----报错
# '''
# class D(object):
#
#     def bar(self):
#         print("D.bar")
#
# class B(D):
#     pass
#     # def bar(self):
#     #     print("B.bar")
#
# class C(D):
#     def bar(self):
#         print("C.bar")
#
# class A(B,C):
#     pass
#     # def bar(self):
#     #     print("A.bar")
#
#
#
# '''新式类实现多继承
# ---A查找-无-----B查找--无----C查找--无-----C查找--无----报错'''
#
# a=A()
# a.bar()




class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性
F.mro()#继承顺序
#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类

#继承顺序
