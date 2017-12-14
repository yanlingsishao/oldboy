#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# #
# class animal:
#     def __init__(self):
#         islife = True
#         isbreathe = True
#         iseat = True
#         isbreed = True
#
class people:
    __zhazha__ = "zhazha"
    def __init__(self,name):
        self.name = name
    def __nimei__(self):
        return "nimei"
    def man(self):

        print("{}出生了，他是个oldboy".format(self.name))

import pymysql

def jj():
    try:
      #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
      conn=pymysql.connect(host='192.168.1.111',user='root',passwd='123456',db='huabei',port=3306,charset='utf8')
      cur=conn.cursor()#获取一个游标
      cur.execute('select id,username,date from dd')
      data=cur.fetchall()
      #print(data)
      for d in data:
        #注意int类型需要使用str函数转义
        print("ID:{}   用户名:{} \t注册时间:{}".format(str(d[0]),d[1],d[2]))
        #print("ID: ",str(d[0]),' 用户名： ',d[1],"   注册时间： ",d[2])
      cur.close()#关闭游标
      conn.close()#释放数据库资源
    except Exception :print("查询失败")

jj()

# class Riven:
#     camp = 'Noxus'
#     def __init__(self,
#                  nickname,
#                  aggressivity=54,
#                  life_value=414,
#                  money=1001,
#                  armor=3
#                  ):


print(people("zhengguojiang").__zhazha__)
print(people("zhengguojiang").__nimei__())
