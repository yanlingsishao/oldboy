# class ParentClass1: #定义父类
#     pass
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(ParentClass1.__bases__)
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

# class Aniaml:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def walk(self):
#         print('%s is walking' %self.name)
#
#     def say(self):
#         print('%s is saying' %self.name)
#
#
# class People(Aniaml):
#     pass
#
# class Pig(Aniaml):
#     pass
#
# class Dog(Aniaml):
#     pass
#
#
# p1=People('obama',50)
# print(p1.name)
# print(p1.age)
# p1.walk()
#
# class Hero:
#     def __init__(self, nickname,
#                  aggressivity,
#                  life_value):
#         self.nickname = nickname
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
# class Garen(Hero):
#     camp='Demacia'
#     def attack(self, enemy):
#         pass
#     def fire(self):
#         print('%s is firing' %self.nickname)
# class Riven(Hero):
#     camp='Noxus'
# g1=Garen('garen',18,200)
# r1=Riven('rivren',18,200)
# # print(g1.camp)
# # print(r1.camp)
# # g1.fire()
# g1.attack(g1)



#派生
# class Hero:
#     def __init__(self, nickname,aggressivity,life_value):
#         self.nickname = nickname
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#     def attack(self, enemy):
#         print('Hero attack')
# class Garen(Hero):
#     camp = 'Demacia'
#
#     def attack(self, enemy): #self=g1,enemy=r1
#         # self.attack(enemy) #g1.attack()
#         Hero.attack(self,enemy)
#         print('from garen attack')
#
#     def fire(self):
#         print('%s is firing' % self.nickname)
# class Riven(Hero):
#     camp = 'Noxus'
# g1 = Garen('garen', 18, 200)
# r1 = Riven('rivren', 18, 200)
# g1.attack(r1)
# # print(g1.camp)
# # print(r1.camp)
# # g1.fire()






class Hero:
    def __init__(self, nickname, aggressivity, life_value):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value
    def attack(self, enemy):
        print('Hero attack')
        enemy.life_value -= self.aggressivity
# print(Hero.__init__)
# print(Hero.attack)
class Garen(Hero):
    camp = 'Demacia'
    def __init__(self, nickname, aggressivity, life_value, script):
        Hero.__init__(self,nickname,aggressivity,life_value)
        # self.nickname = nickname
        # self.aggressivity = aggressivity
        # self.life_value = life_value
        self.script = script
    def attack(self, enemy):  # self=g1,enemy=r1
        # self.attack(enemy) #g1.attack()
        Hero.attack(self, enemy)
        print('from garen attack')
    def fire(self):
        print('%s is firing' % self.nickname)
# g1=Garen('garen',18,200) #Garen.__init__(g1,'garen',18,200)
g1=Garen('garen',18,200,'人在塔在') #Garen.__init__(g1,'garen',18,200)
print(g1.script)












