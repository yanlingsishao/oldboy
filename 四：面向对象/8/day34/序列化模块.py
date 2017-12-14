


# d={"河北":["廊坊","保定"],"湖南":["长沙","韶山"]}
#
# s=str(d)
# with open("data","w") as f:
#     f.write(s)

# with open("data") as f2:
#     s2=f2.read()
#     d2=eval(s2)
#
# print(d2["河北"]) # '{"河北":["廊坊","保定"],"湖南":["长沙","韶山"]}'

# print(eval("12+34*34"))

import json


import json


# i=10
# s='hello'
# t=(1,4,6)
# l=[3,5,7]
# d={'name':"yuan"}
#
# json_str1=json.dumps(i)
# json_str2=json.dumps(s)
# json_str3=json.dumps(t)
# json_str4=json.dumps(l)
# json_str5=json.dumps(d)
#
# print(json_str1)   #'10'
# print(json_str2)   #'"hello"'
# print(json_str3)   #'[1, 4, 6]'
# print(json_str4)   #'[3, 5, 7]'
# print(json_str5)   #'{"name": "yuan"}'









# # d={"河北":["廊坊","保定"],"湖南":["长沙","韶山"]}
#
# d={'name':"egon"}
#
# # s=json.dumps(d)  #   将字典d转为json字符串---序列化
# #
# # print(type(s))
# # print(s)
# #
# #
# # f=open("new",'w')
# #
# # f.write(s)
# #
# # f.close()
#
# # -------------- dump方式
#
# # f=open("new2",'w')
# # json.dump(d,f)#---------1 转成json字符串 2 将json字符串写入f里
# #
# # f.close()
#
#
# #-----------------反序列化
#
# # f=open("new")
# #
# # data=f.read()
# #
# # data2=json.loads(data)
# #
# # print(data2["name"])


#------练习

# f=open("new3")
# data=f.read()
#
# ret=json.loads(data)
# # ret=[123]
# print(type(ret[0]))



#----------------------------------pickle--------------------


import pickle


import datetime

t=datetime.datetime.now()


# d={"data":t}

# json.dump(d,open("new4","w"))

#d={"name":"alvin"}

# s=pickle.dumps(d)
# print(s)
# print(type(s))
#
# f=open('new5',"wb")
#
# f.write(s)
# f.close()


# f=open("new5","rb")
#
# data=pickle.loads(f.read())
#
# print(data)








