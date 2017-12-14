#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-13 15:05
# @Author  : Jerry Wang
# @Site    : 
# @File    : fabfile.py
# @Software: PyCharm
import datetime
class Student():
    _id_num = 0
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year,cls._id_num)

    def __init__(self):
        self.dd = Student._id_gen()


y = Student()

print(y.dd)