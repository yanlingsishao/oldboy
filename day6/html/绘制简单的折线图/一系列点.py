#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-6 17:02
# @Author  : Jerry Wang
# @Site    : 
# @File    : 一系列点.py
# @Software: PyCharm
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values,y_values,s=100)
plt.show()
