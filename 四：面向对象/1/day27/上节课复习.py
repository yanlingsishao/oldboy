# list
# int
# tuple


#在python3中，所有的类都是新式类
#
# class A:pass
# print(A.__bases__)
#
#
#
#
# #在python2中，新式类
# class B(object):pass
# class C(B):pass
#
#
# print(B.__bases__)
# print(C.__bases__)
#
#
#
# #在python2中，经典类
# class D:pass
# print(D.__bases__)


# class Student:
#     country = 'China'
#
#     def __init__(self, ID, NAME, SEX, PROVINCE):
#         self.id = ID
#         self.name = NAME
#         self.sex = SEX
#         self.province = PROVINCE
#
#     def search_score(self):
#         print('tell score')
#
#     def study(self): #self=s1
#         print('study',self)
#类属性：特征（变量）和技能（函数）

#类的用法:实例化，属性引用
# s1 = Student('371818181818181', 'cobila', 'female', 'shanxi')
    #Student.__init__(s1,'371818181818181','cobila','female','shanxi')
    # s1.id='371818181818181'
    # s1.name='cobila'
    # s1.sex='female'
    # s1.province='shanxi'

# print(Student.country)
# print(Student.__init__)
# print(Student.study)
# print(Student.search_score)

# Student.__init__(s1,'371818181818181','cobila','female','shanxi')
# Student.study(s1)

# Student.x=1
# print(Student.x)
# x=10000000
# print(Student.x)

# del Student.x
# print(Student.x)
#
# print(Student.study)
# del Student.study
# print(Student.study)

# Student.country='xxxxx'
# print(Student.country)


# class Struct:pass
# Struct.x=1
# Struct.y=2
# Struct.res=Struct.x+Struct.y
# print(Struct.res)



# class Student:
#     country = 'China'
#
#     def __init__(self, ID, NAME, SEX, PROVINCE):
#         self.id = ID
#         self.name = NAME
#         self.sex = SEX
#         self.province = PROVINCE
#
#     def search_score(self):
#         print('tell score')
#
#     def study(self): #self=s1
#         print('study',self)
#
# s1 = Student('371818181818181', 'cobila', 'female', 'shanxi')

#对象也称为实例
#对象的属性：对象本身就只有特征（变量）

#对的用法：属性引用
# print(s1.id,s1.name,s1.sex,s1.province)
# s1.weight=100
#
# weight=1111111111111111111111111111111111111111111111
# print(s1.weight)
# # del s1.weight
# # print(s1.weight)
#
# s1.id=123
# print(s1.id)



#类的名称空间与对象的名称空间
# x=123123123123
# class Student:
#     country = 'China'
#
#     def __init__(self, ID, NAME, SEX, PROVINCE):
#         self.id = ID
#         self.name = NAME
#         self.sex = SEX
#         self.province = PROVINCE
#
#
#     def search_score(self):
#         print('tell score')
#
#     def study(self): #self=s1
#         print('study',self)
#     def walk(self):
#         print('name:%s is walking' %self.name)
#
# s1 = Student('371818181818181', 'cobila', 'female', 'shanxi')
# s2 = Student('371818181sadf818181', 'cobilamei', 'femaleasfd', 'shasdfanxi')
#
#
# # print(Student.__dict__) #查看类的名称空间
# # print(Student.country)
# # print(s1.__dict__)#查看对象的名称空间
# # print(s1.id)
# # s1.country="123123123"
# # print(id(s1.country))
# # print(id(s2.country))
# # print(id(Student.country))
# #
# print(s1.study,id(s1.study))
# print(Student.study,id(Student.study))
# #绑定方法的核心在于‘绑定’，唯一绑定一个确定的对象
# s1.walk()
# s2.walk()



class Riven:
    camp='Noxus'  #所有玩家的英雄(锐雯)的阵营都是Noxus;
    def __init__(self,nickname,aggressivity=54,life_value=414): #英雄的初始攻击力54;
        self.nickname=nickname  #为自己的锐雯起个别名;
        self.aggressivity=aggressivity #英雄都有自己的攻击力;
        self.life_value=life_value #英雄都有自己的生命值;
    def attack(self,enemy):   #普通攻击技能，enemy是敌人;
        enemy.life_value-=self.aggressivity #根据自己的攻击力，攻击敌人就减掉敌人的生命值。

class Garen:
    camp='Noxus'  #所有玩家的英雄(锐雯)的阵营都是Noxus;
    def __init__(self,nickname,aggressivity=54,life_value=414): #英雄的初始攻击力54;
        self.nickname=nickname  #为自己的锐雯起个别名;
        self.aggressivity=aggressivity #英雄都有自己的攻击力;
        self.life_value=life_value #英雄都有自己的生命值;
    def attack(self,enemy):   #普通攻击技能，enemy是敌人;
        enemy.life_value-=self.aggressivity #根据自己的攻击力，攻击敌人就减掉敌人的生命值。


#对象之间的交互
# r1=Riven('芮雯雯')
# g1=Garen('草丛轮')
# print(r1.life_value)
# g1.attack(r1)
# print(r1.life_value)


# name=input('your nickname: ')
# r1=Riven(name)








