#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import os
import re
from mysql_conn import my_sql


data_file="..\\data\\"
class handle_file(object):
    def eachfile(self):
        '''查找文件'''
        self.dic_file = {}
        self.pathdir = os.listdir(data_file)
        for i in self.pathdir:
            child = "{}{}".format(data_file,i)
            childdir = os.listdir(child)
            self.dic_file.update({i:childdir})
        return self.dic_file

    def readfile(self,path):
        '''读取文件
        :rtype: object
        '''
        with open(path,"r",encoding="utf-8") as file:
            values = []
            lines = file.readlines()
            if len(lines) == 1:
                return False
            else:
                for line in lines[1:]:
                    line=line[:-1]
                    re_line = line.split("|")
                    values.append(re_line)
                    #print(line)
                return values

PP = ["BALANCECHANGE","RECHARGE","TRANSACTION","WITHDRAW"]

def update_sql():
    count = 0
    x = handle_file()
    y = x.eachfile()
    dir_list = list(y.keys())
    for first_dir in dir_list:#06 07
        for i in y.get(first_dir):
            for j in PP:
                l = re.findall(".+{}.+".format(j),i)
                if l:
                    get_data = x.readfile("{}{}\\{}".format(data_file,first_dir,i))
                    sql_list_name=j.lower()#表名
                    if get_data != False:
                        for single_data in get_data:
                            ll = {"balancechange":'''INSERT INTO balancechange(file_name,user_id,
                                            roll_into_amount,roll_out_amount,account_balance) VALUES
                                            ('{}','{}')'''.format(i,"','".join(single_data)),
                                  "recharge":'''INSERT INTO recharge(file_name,merchant_order_number,
                                            depository_order_number,trade_type,
                                            trade_amount,trade_status,finish_time,payment_company_code,
                                            platform_user_id,business_source,note) VALUES
                                            ('{}','{}')'''.format(i,"','".join(single_data)),
                                  "transaction":'''INSERT INTO transaction(file_name,merchant_order_number,
                                                  depository_order_number,trade_type,
                                                  trade_amount,trade_status,finish_time,object_number,
                                                  out_money_party,in_money_party,note) VALUES
                                                  ('{}','{}')'''.format(i,"','".join(single_data)),
                                  "withdraw":'''INSERT INTO withdraw(file_name,merchant_order_number,
                                                  depository_order_number,trade_type,
                                                  trade_amount,trade_status,finish_time,payment_company_code,
                                                  platform_user_id,note) VALUES
                                                  ('{}','{}')'''.format(i,"','".join(single_data)),
                                  }
                            mysql_co = my_sql()
                            k = mysql_co.mysql_exec(ll.get(sql_list_name))
                            count += 1
                            print("{}执行成功".format(count))
            # print("{}执行完毕".format(j))
    mysql_co.close()









update_sql()

# i = x.eachfile()
# print(i)
# y = x.readfile("..\\data\\06\\20170621_M20002661169_TRANSACTION.txt")
# print(y)
# p = x.update_sql()
# print(p)

