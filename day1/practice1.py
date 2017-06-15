#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# 1、使用while循环输入 1 2 3 ... 8 9 10
# i = 1
# while True:
#     if i <= 10:
#         print(i)
#         i += 1
#     else:
#         break

# 2、求1 - 100的所有数的和
#(1)
# n = 1
#
# for i in range(1,100):
#         i += 1
#         n += i
# print(i)
# print(n)
#2)
# n = 1
# sum = 0
# while True:
#     if n <= 100:
#         sum += n
#         n += 1
#     else:
#         break
# print(sum)



# 3、输出 1-100 内的所有奇数
#(1)
# x = 1
# for i in range(1,100):
#     if x < 100:
#         print (x)
#         x += 2
#         i += 1
#     else:
#         break

#(2)
# i = 1
# while True:
#     if i < 100:
#         print(i)
#         i += 2
#     else:
#         break
#(3)
# n = 1
# while n<101:
#     temp = n % 2
#     if temp == 0:
#         pass
#     else:
#         print(n)
#     n += 1

# 4、输出1 - 100内的所有偶数
#(1)
# x = 2
# for i in range(1,100):
#     if x <= 100:
#         print (x)
#         x += 2
#         i += 1
#     else:
#         break

# (2)
# i = 2
# while True:
#     if i <= 100:
#         print(i)
#         i += 2
#     else:
#         break
# (3)
# n = 1
# while n<101:
#     temp = n % 2
#     if temp == 0:
#         print(n)
#     else:
#         pass
#     n += 1

# 5、求1-2+3-4 ... 99的值

# n = 1
# s = 0
# while n < 100:
#     temp = n % 2
#     if temp == 0:
#         s -= n
#     else:
#         s += n
#     n += 1
# print(s)


