#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import pymysql
import configparser
from logger import MyLogger

CONFIG_FILE = '../conf/config.cfg'

config = configparser.ConfigParser()
config.sections()
config.read(CONFIG_FILE,encoding='utf-8')


#####DB Config start#########################
__db_host=config['db']['__db_host']
__db_user=config['db']['__db_user']
__db_port=int(config['db']['__db_port'])
__db_database=config['db']['__db_database']
__db_password=config['db']['__db_password']


def mysql_exec(db_config):
    try:
        #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn=pymysql.connect(host=__db_host,user=__db_user,passwd=__db_password,db=__db_database,port=__db_port,charset='utf8')
        cur=conn.cursor()#获取一个游标
        cur.execute(db_config)
        conn.commit()
        data=cur.fetchall()
        cur.close()#关闭游标
        conn.close()#释放数据库资源
        MyLogger.info("sql execute successfully [{}]".format(db_config))
        return data
    except Exception :
        print("sql失败")
        MyLogger.error("sql execute failure [{}]".format(db_config))
        return False

def get_url():
    try:
        result = do_get()
        my_logger.write_info("get True;", "get_url", result)
        return True

    except Exception as err:
        # print (e)
        my_logger.write_err("get False;", "get_url", err)
        return False

# data = mysql_con("select * from hb_borrow")
# print (data)