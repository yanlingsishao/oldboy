#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月16日
@author: WangQiyuan

'''

shop_inf = {
    "笔":{"price":10},
    "笔记本":{"price":10},
    "杯子":{"price":300},
}
user_inf = {
    "liming":{"passwd":"1234","user_balance":400,"recharge_inf":["暂无充值记录"],"buy_inf":["暂无购买记录"]},
    "wangqiyuan":{"passwd":"123456","user_balance":290,"recharge_inf":["暂无充值记录"],"buy_inf":["暂无购买记录"]},
}

def passwd(user):#用户信息信息
    user_infor = user_inf.get(user)#获取用户完整信息
    user_pass = user_infor.get("passwd")#获取用户密码
    user_balance = user_infor.get("user_balance")#获取用户余额
    return (user_infor,user_pass,user_balance)

def shop(goods):#商品信息
    shop_infor = shop_inf.get(goods)#获取完整信息
    shop_price = shop_infor.get("price")#获取价格
    return (shop_infor,shop_price)

def shop_buy(user,goods,num):
    shop_price_1 = shop(goods)[1]#购买的产品价格
    user_balance_1 = passwd(user)[2]#用户余额
    now_balance = user_balance_1 - shop_price_1*num#消费后余额
    return (now_balance,shop_price_1,user_balance_1,num)

def recharge(user,amount):#充值
    balance = passwd(user)[2]#用户当前余额
    passwd(user)[0].update({"user_balance":balance+amount})#用户信息更新
    #newbalance = user_inf.update({"user_balance":newvalue})
    user_infor = user_inf.get(user)
    return (balance+amount,user_infor)

def rechar(userx,count):
    now_recharge = int(input("请输入要充值的金额："))
    current_recharge = recharge(userx, now_recharge)  # 充值
    user_inf[userx]["user_balance"] = current_recharge[0]  # 充值完成
    new_recharge_inf = "第{}笔充值为{}".format((count + 1), now_recharge)  # 新充值信息
    old_recharge_inf = user_inf[userx]["recharge_inf"]  # 充值信息
    old_recharge_inf.append(new_recharge_inf)  # 增加新充值信息进库
    print("充值成功，现在的余额是", user_inf[userx]["user_balance"], "元")  # 打印充值成功及余额
    old_recharge_inf[0] = "已有充值"  # 购物历史信息变更
    print(user_inf[userx]["recharge_inf"][count + 1])  # 打印当前笔数充值钱数
    count += 1

def shop_info(userx,*args):#购物信息
    print("购买记录：")
    if user_inf[userx]["buy_inf"] != ["暂无购买记录"]:
        for buy_inf_1 in user_inf[userx]["buy_inf"]:#打印购买记录
            print(buy_inf_1)
    else:
        print("无购买信息")

def buys(current_buy,userx,count1):#购买函数(jj:购买的物品，userx:当前登录用户)
    current_buy_balance = shop(current_buy)[1]  # 当前商品价格
    buy_num = int(input("购买几个："))#输入购买数量
    if shop_buy(userx, current_buy, buy_num)[0] < 0:#验证余额
        print("您的余额不足")
    else:#余额足够买商品
        # passwd(userx)[0].update({"user_balance":shop_buy(userx,jj)[2]})
        user_inf[userx]["user_balance"] = shop_buy(userx, current_buy, buy_num)[0]  ##购买成功
        new_buy_inf = "第{}次购买了{}个{},花费了{}元".format((count1 + 1), buy_num, current_buy, current_buy_balance * buy_num)  # 新购买信息
        buy_inf = user_inf[userx]["buy_inf"]  # 充值信息
        buy_inf.append(new_buy_inf)  ## 增加新充值信息进库
        print(new_buy_inf)  # 打印购买成功及余额
        buy_inf[0] = "已有购买"
        print("您的余额为{}元".format(user_inf[userx]["user_balance"]))

def login_demo(userx):#登录界面
    print("欢迎登录".center(30, "*"))
    print("".center(33, "*"))
    print("您当前的余额是{}元".format(passwd(userx)[2]))

def balance_inquire(userx,*args):
    print("您当前的余额是{}元".format(passwd(userx)[2]))

def login_portal(userx,count):#功能界面
    while True:
        all_function = input("请输入您的操作（充值，购买，购物信息，商品查询，充值查询，余额查询（q退出账号））")
        # 定义功能字典
        func_dic = {"充值": rechar,"购物信息":shop_info,"充值查询":recharge_query,"余额查询":balance_inquire}
        if all_function == "购买":
            buy(userx, count1)#执行购买函数
        elif all_function == "q":#退出账号
            shop_info(userx)  # 输出购买信息
            print("退出账号".center(30, "*"))
            break
        elif all_function in func_dic.keys():#执行字典函数
            func_dic.get(all_function)(userx,count)

def buy(userx,count1):#购买
    for i in shop_inf.keys():#列出商品信息
        print(i, shop(i)[1], "元")
    while True:
        current_buy = input("请输入您要购买的物品(q退出):")
        if current_buy == 'q':
            break
        buys(current_buy, userx, count1)
        count1 += 1

def recharge_query(userx,*args):#充值查询
    if user_inf[userx]["recharge_inf"] != ["暂无充值记录"]:
        for rec_inf in user_inf[userx]["recharge_inf"][1:]:
            print(rec_inf)
    else:
        print("无充值信息")

def atm(count,count1):#入口
    while True:
        begin_oper = input("请输入操作：1.登录 2.退出")#登退操作
        if begin_oper == "1":#登录
            userx = input("请输入账号:")#输入账号
            passwdx = input("请输入密码: ")#输入密码
            if userx not in user_inf.keys():#验证账号是否存在
                print("无此用户")
                continue
            use_pass = passwd(userx)[1]#获取账号密码
            if passwdx == use_pass:#验证密码是否正确
                login_demo(userx)#正确，登录界面
                login_portal(userx, count)#功能界面
            else:
                print("密码不正确")
        elif begin_oper == "2":#退出
            break


if __name__ == "__main__":
    count = 0
    count1 = 0
    atm(count,count1)