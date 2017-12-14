# #coding:utf-8
# #super在python2中的用法：
#     # 1:super(自己的类,self).父类的函数名字
#     # 2：super只能用于新式类
# class People(object):
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def walk(self):
#         print('%s is walking' %self.name)
# class Chinese(People):
#     country='China'
#     def __init__(self,name,sex,age,language='Chinese'):
#         # self.name=name
#         # self.sex=sex
#         # self.age=age
#         # People.__init__(self,name,sex,age)
#         super(Chinese,self).__init__(name,sex,age)
#         self.language=language
# c=Chinese('egon','male',18)
# print c.name,c.age,c.sex,c.language



#在python3中
class People:
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex
    def walk(self):
        print('%s is walking' %self.name)
class Chinese(People):
    country='China'
    def __init__(self,name,sex,age,language='Chinese'):
        # self.name=name
        # self.sex=sex
        # self.age=age
        # People.__init__(self,name,sex,age)
        super(Chinese,self).__init__(name,sex,age)
        self.language=language
    def walk(self,x):
        super().walk()
        print('子类的x',x)
c=Chinese('egon','male',18)
# print(c.name,c.age,c.sex,c.language)
c.walk(123)