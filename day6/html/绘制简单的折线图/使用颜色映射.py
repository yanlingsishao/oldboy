#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-6 17:16
# @Author  : Jerry Wang
# @Site    : 
# @File    : 使用颜色映射.py
# @Software: PyCharm
import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolors="none",s=40)

plt.show()
plt.savefig("squares_plot.png",bbox_inches='tight')