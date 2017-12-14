#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
format_dict={
    "ymd":'{0.year}{0.mouth}{0.day}',
    "y:m:d":'{0.year}:{0.mouth}:{0.day}',
    "m-d-y":'{0.mouth}-{0.day}-{0.year}'
}
class Date:
    def __init__(self,year,mouth,day):
        self.year=year
        self.mouth=mouth
        self.day=day

    def __format__(self, format_spec):
        print("我执行了")
        if not format_spec or format_spec not in format_dict:
            format_spec="ymd"
        f=format_dict[format_spec]
        return f.format(self)

d1=Date(2017,9,25)
format(d1)
print(format(d1,"y:m-d"))


# x = '{0.year}{0.mouth}{0.day}'.format(d1)
# y = '{0.year}:{0.mouth}:{0.day}'.format(d1)
# z = '{0.mouth}-{0.day}-{0.year}'.format(d1)
# print(x)
# print(y)
# print(z)
