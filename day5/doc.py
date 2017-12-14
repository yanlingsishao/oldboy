#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
class Foo:
    '''你好'''
    def x(self)->"hello":
        return self

    pass

class Bar(Foo):
    pass


def x() -> "hello":
    pass

# print(x.__annotations__)
# print(Bar.__doc__)
print(Foo)
print(Bar.__dict__)
print(Foo.__doc__)
# print(Bar.__dict__)
print(Foo.__dict__)