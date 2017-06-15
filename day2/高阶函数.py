#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月16日
@author: WangQiyuan

'''
#高阶函数定义
#1.函数接收的参数是一个函数名
#2.函数的返回值是一个函数名
#3.满足上述条件任意一个,都可称之为高阶函数
#(1)
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
#(2)
# def foo():
#     print("nihao")
# def test(func):
#     return func
# # res=test(foo)
# # res()
# foo=test(foo)
# foo()
#(3)不修改foo源代码，不修改foo调用方式
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

# 函数嵌套
def father(name):
    print('from father %s' %name)
    def son():

        print('from son')
        def grandson():
            print('from grandson')
        grandson()
    son()

father('王琦渊')

# 闭包，作用域的一种体现



# num_1=[1,2,10]
# ret=[]
# for i in num_1:
#     ret.append(i**2)
#
# print(ret)


# def map_test(func,array):
#     ret =[]
#     for i in array:
#         res=func(i)
#         ret.append(res)
#     return ret
#
# gg = list(map(lambda x:x+1,num_1))
# print(gg)
# movie_people=['alex','wupeiqi','yuanhao','sb_alex','sb_wupeiqi','sb_yuanhao']
# def filter_test(func,array):
#     ret=[]
#     for i in array:
#         if func(i):
#             ret.append(i)
#     return ret
#
# print(filter_test(tell_sb,movie_people))


#函数filter,返回可迭代对象
# print(list(filter(lambda x:x.startswith('sb'),movie_people)))


from functools import reduce
#map 处理序列中的每个元素，得到的结果是一个列表，该列表元素个数及位置于原来一样
# print(list(map(lambda x:x+2, [1, 2, 3])))
#>>>[3, 4, 5]

# print(list(map(lambda x,y:x+y, [2, 3], [1, 2])))
# >>>[3, 5]
#
# 处理一个序列，然后把序列进行和并操作
# print(reduce(lambda x,y:x+y, [1,2,3,4],10))
# >>>20
#
# filter 遍历序列中的每个元素，判断每个元素得到布尔值，如果是True则留下来，过滤
# print(list(filter(lambda x:x%2==1, range(20))))
# >>>[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# zip
# p={"name":1,"age":50,"gender":"none"}
# print(list(zip(("a","b","c","h"),(1,2,3))))
# print(list(zip(p.keys(),p.values())))

# l=[1,2,3,-5]
# print(max(l))
# dic = {'age1':18,'age2':10}
# print(max(dic))
# print(max(dic.values()))
# print(max(zip(dic.values(),dic.keys())))#结合zip比较value。出key
#1、max函数处理的是可迭代对象，相当于一个for循环取出各个元素进行比较，注意，不同类型之间不能进行比较
#2、每个元素间进行比较，是从每个元素的每一个位置依次比较，如果这一个位置分出大小，后面的就不需要比较了，直接得出这两元素的大小。

# people = [
#     {"name":"alex","age":1000},
#     {"name":"wupeiqi","age":10000},
#     {"name":"zhazha","age":9000},
#     {"name":"wangqiyuan","age":18}
# ]
# print(max(people,key=lambda dic:dic["age"]))
# ret=[]
# for item in people:
#     ret.append(item["age"])
# print(ret)
# max(ret)

