#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''

# import pymysql
#
# conn = pymysql.connect(host="192.168.1.1",port=3306,user="root",passwd="123",db="t1")
# cursor = conn.cursor()
# conn.commit()
# cursor.close()
# conn.close()

import pymysql
import configparser
from logger import MyLogger

class my_sql(object):
    def __init__(self):
        CONFIG_FILE = '../conf/config.cfg'
        config = configparser.ConfigParser()
        config.sections()
        config.read(CONFIG_FILE, encoding='utf-8')
        self.__db_host=config['db']['__db_host']
        self.__db_user=config['db']['__db_user']
        self.__db_port=int(config['db']['__db_port'])
        self.__db_database=config['db']['__db_database']
        self.__db_password=config['db']['__db_password']

    def mysql_exec(self,db_config):
        try:
            #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
            self.conn=pymysql.connect(host=self.__db_host,user=self.__db_user,
                                 passwd=self.__db_password,db=self.__db_database,port=self.__db_port,charset='utf8')
            self.cur=self.conn.cursor()#获取一个游标
            self.cur.execute(db_config)
            self.conn.commit()
            #self.conn.commit()
            self.data=self.cur.fetchall()
            #cur.close()#关闭游标
            #conn.close()#释放数据库资源
            MyLogger.info("sql execute successfully [{}]".format(db_config))
            return self.data
        except Exception as e:
            print("sql失败")
            self.conn.rollback()#发生错误回滚
            MyLogger.error("[{}]sql execute failure [{}]".format(e,db_config))
            return False

    def get_chone(self):
        row_2 = self.cur.fetchall()
        return row_2

    def close(self):
        self.cur.close()
        self.conn.close()


# x = my_sql()
# x.mysql_exec("select * from user")
# y = x.get_chone()
# print(y)
# x.close()