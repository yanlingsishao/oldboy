#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
'''
#账号状态
普通用户状态：common：
            存款，取款，查询余额，修改密码，转账，账单打印
花呗用户状态：huabei：
            common权限，借款，还款，
逾期用户状态：overdue
            common权限，还款，账单发邮箱
冻结用户状态：lockuser：
            无权限
#花呗模块，功能
1、账号定期还款
    每月8号开始还款，还款失败，则更改账号status为逾期状态
2、定期账单
    还款后的的账单
3、借款。
4、逾期还款，
    超出一个月，账号冻结，1-30天之内，每10天加一次息。1--10，一共收借款的0.1。11--20，一共收借款的0.2  21--30，一共收借款的0.3
5、逾期
'''
import manager
from logger import MyLogger
import json
import mysql_conn
import time
#----------借款func-------------------------------------.
# def load_rule(user,monnum,userstatus):
#     if userstatus == "huabei":
#
#     else:
#         print("没有借款权限！！！")
#
#
# def load_func(*args):
#     pass

#-------------------升级花呗会员——————————————————

now_date=time.strftime("%Y%m%d")#查询当前日期



#花呗默认开启额度为3000
def huabei_rule(user):#根据余额判断是否可以升级
    now_balance=float(manager.get_user_onevalue(user,"balance"))#取当前余额
    if now_balance >= 12000:
        return True
    else:
        return False

def huabei_update(user):#更改状态为花呗
    if huabei_rule(user) == True:
        manager.change_user_info(user,"user_status","huabei")
        manager.change_user_info(user,"user_huabei","3000")
        #dic = {user: {user: {"借款事项": [], "花呗额度": [3000], "花呗剩余额度": [3000],"用户借款": [0], "用户还款": [0]}}}
        data_file = (user,"",3000,00000000,0,3000)
        table_name = "hb_borrow"
        sql_insert = '''insert into {}(username,borrow_done,huabei_limit,borrow_date,isrepayment,huabei_residue_limit) values{}'''.format(table_name,data_file)
        data = mysql_conn.mysql_exec(sql_insert)
        print('''您好，花呗会员开启，您当前额度为3000
请重新登录''')

    else:
        print( "抱歉，您没有升级资格，您还需存更多的钱")
        MyLogger.warning("没有升级资格")



#----------借款func-------------------------------------.
# class borrow:
#     def __init__(self,user):
#         self.user = user
def borrow_rule(user):
    userstatus=manager.get_user_onevalue(user,"user_status")
    if userstatus == "huabei":
        user_huabei_balance=manager.get_user_onevalue(user,"user_huabei")
        return user_huabei_balance
    else:
        return False

# 借款账单
def add_borrow_info(user, borrow_done, borrow_num):
    add_borrow = '''insert into hb_borrow_info(username,borrow_info,borrow_num,borrow_date) values("{}","{}",{},{})'''.format(user, borrow_done, borrow_num, now_date)
    data = mysql_conn.mysql_exec(add_borrow)

def show_borrow_info(user):
    while True:
        x = input("打印借款账单(1),打印还款账单(2),返回上一级(q)")
        if x == "1":
            all_borrow_info='''SELECT borrow_info,borrow_num,borrow_date from hb_borrow_info WHERE username = "{}"'''.format(user)
            data = mysql_conn.mysql_exec(all_borrow_info)
            li_data=list(data)
            if data:
                for i in li_data:
                    print("[{}] {} 借款 {} 元".format(i[2],i[0],i[1]))
            elif not data:
                print("没有借款数据")
                break
        elif x == "2":
            all_repayment_info='''SELECT repayment_num,repayment_date from hb_repayment_info WHERE username = "{}"'''.format(user)
            data = mysql_conn.mysql_exec(all_repayment_info)
            li_data=list(data)
            if data:
                for i in li_data:
                    print("[{}] 还款 {} 元".format(i[1],i[0]))
            elif not data:
                print("没有还款数据")
                break
        elif x == "q":
            break
        else:
            continue



#
# show_borrow_info("wangqiyuan")
    # def islimit(self):#判断是否是借过款的用户
    #     user=self.user
    #     sql_select_isuser = '''SELECT * FROM hb_borrow WHERE username = "{}"'''.format(user)
    #     sql_select_isuser_data = mysql_conn.mysql_exec(sql_select_isuser)
    #     return sql_select_isuser_data

    # def isselect(self):
    #     islimit=borrow.islimit()
    #     if islimit == None:
    #         print("还没有借过款")
    #     else:
    #         print(jj)



def borrow_(user):
    #user=self.user
    #查出剩余额度
    select_resudye_limit='''SELECT huabei_residue_limit FROM hb_borrow WHERE username = "{}"'''.format(user)
    sql_select_used_limit = mysql_conn.mysql_exec(select_resudye_limit)
    bor_rule = borrow_rule(user)  # 不变的额度
    now_balance = float(manager.get_user_onevalue(user, "balance") ) # 现在的余额
    if bor_rule != False:
        print("你当前的可用花呗额度为{}元".format(sql_select_used_limit[0][0]))
        huabei_done = input("你要借钱做什么：")
        wileborrow_huabei = float(input("您要从花呗借多少钱："))  # 借款额
        if wileborrow_huabei <= sql_select_used_limit[0][0]:#借的钱与剩余额度比较
            huabei_residue_limit=float(sql_select_used_limit[0][0])-wileborrow_huabei
            sql_insert ='''UPDATE hb_borrow SET borrow_done= "{}",
                            huabei_residue_limit = {}, borrow_date = {}, isrepayment = 0
                            WHERE username = "{}"'''.format(huabei_done,huabei_residue_limit,now_date,user)
            mysql_conn.mysql_exec(sql_insert)
            borrowd=manager.change_user_info(user, "balance",str(now_balance+wileborrow_huabei))
            add_borrow_info(user,huabei_done,wileborrow_huabei)
            print("加载入文件完成...")
            return borrowd
        else:
            print("超过额度，请联系管理员提额")
    else:
        print("没有此权限")






#print(time.strftime("%Y%m%d"))
#
#
# data = borrow("wangqiyuan").borrow_()
def add_repayment_info(user,repayment_num):
    add_repayment = '''insert into hb_repayment_info(username,repayment_num,repayment_date) values("{}",{},{})'''.format(user,repayment_num, now_date)
    data = mysql_conn.mysql_exec(add_repayment)


#还款功能
def repayment(user):
    select_repayment = '''SELECT ifnull(huabei_limit,0)-ifnull(huabei_residue_limit,0) FROM hb_borrow WHERE username = "{}"'''.format(user)
    select_date = '''SELECT borrow_date FROM hb_borrow WHERE username = "{}"'''.format(user)
    sql_select_repayment = mysql_conn.mysql_exec(select_repayment)#待还
    sql_select_date = mysql_conn.mysql_exec(select_date)
    print("[{}]借款{}元待还".format(sql_select_date[0][-1],sql_select_repayment[0][0]))

    while True:
        x = input("确定还款(1),返回上一级(q)")
        if x == "1":
    # print(sql_select_repayment[0][0])
            if sql_select_repayment != None and sql_select_repayment[0][0] > 0:#判断还款额
                now_balance=manager.get_user_onevalue(user,"balance")
                huabei_limit=float(manager.get_user_onevalue(user,"user_huabei"))
                print(sql_select_repayment[0][0])
                change_balance = float(now_balance) - float(sql_select_repayment[0][0])#更改后的余额
                if float(now_balance) >= sql_select_repayment[0][0]:
                    #manager.change_user_info(user, "balance",(now_balance-sql_select_repayment))#还款
                    sql_insert = '''UPDATE hb_borrow SET  huabei_residue_limit = {},isrepayment = 1 WHERE username = "{}"'''.format(huabei_limit,user)
                    mysql_conn.mysql_exec(sql_insert)
                    now_repayment= mysql_conn.mysql_exec(select_repayment)#待还
                    add_repayment_info(user,sql_select_repayment[0][0])
                    if now_repayment[0][0] == 0:
                        manager.change_user_info(user, "balance",str(change_balance))
                        print("还款成功")
                        break
                else:
                    print("余额不足，请尽快充值还款")
                    break
            else:
                print("无需还款")
                break
        elif x=="q":break
        else:continue



