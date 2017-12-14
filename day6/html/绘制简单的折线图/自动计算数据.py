#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-6 17:05
# @Author  : Jerry Wang
# @Site    : 
# @File    : 自动计算数据.py
# @Software: PyCharm
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,s=40)
plt.axis([0,1100,0,1100000])
plt.show()