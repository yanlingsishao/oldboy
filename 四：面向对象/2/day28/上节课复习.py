class Garen:        #定义英雄盖伦的类，不同的玩家可以用它实例出自己英雄;
    camp='Demacia'  #所有玩家的英雄(盖伦)的阵营都是Demacia;
    n=0
    # hobby=[]
    def __init__(self,nickname,aggressivity=58,life_value=455): #英雄的初始攻击力58...;
        self.nickname=nickname  #为自己的盖伦起个别名;
        self.aggressivity=aggressivity #英雄都有自己的攻击力;
        self.life_value=life_value #英雄都有自己的生命值;
        Garen.n+=1
        self.hobby=[]
    def attack(self,enemy):   #普通攻击技能，enemy是敌人;
        enemy.life_value-=self.aggressivity #根据自己的攻击力，攻击敌人就减掉敌人的生命值。

# g1 = Garen('草丛伦')
# g2 = Garen('草丛伦2')
# g3 = Garen('草丛伦3')
# print(g1.hobby,id(g1.hobby))
# print(g2.hobby,id(g2.hobby))
# print(g3.hobby,id(g3.hobby))
# #
# # # g1.camp='123123123123'
# g1.hobby.append('g1 hobby')
# g2.hobby.append('g2 hobby')
# g3.hobby.append('g3 hobby')
# print(g1.hobby)


#类的两种用法：实例化和属性引用
#一：实例化
# g1 = Garen('草丛伦')
# print(g1.__dict__)


#二：属性引用，类的属性就两种:变量和函数
# print(Garen.camp)
# print(Garen.xxxx)
# print(Garen.attack123)
# print(Garen.__dict__)
# print(Garen.camp)
# print(Garen.attack) #'attack'
#
# Garen.camp='123123123123123'
# Garen.x=123  #Garen.__dict__['x']=123
# print(Garen.__dict__)


# Garen.x=1
# print(Garen.__dict__)

# del Garen.camp
# print(Garen.__dict__)


#实例就一种用法：属性引用，且实例本身就只有
# g1 = Garen('草丛伦')
# print(g1.nickname)
# print(g1.aggressivity)
# print(g1.life_value)
#增，删，改，查实例属性，略



#类的名称空间与实例的名称空间

#类的变量是所有对象共享的
class Garen:        #定义英雄盖伦的类，不同的玩家可以用它实例出自己英雄;
    camp='Demacia'  #所有玩家的英雄(盖伦)的阵营都是Demacia;
    n=0
    # hobby=[]
    def __init__(self,nickname,aggressivity=58,life_value=455): #英雄的初始攻击力58...;
        self.nickname=nickname  #为自己的盖伦起个别名;
        self.aggressivity=aggressivity #英雄都有自己的攻击力;
        self.life_value=life_value #英雄都有自己的生命值;
        Garen.n+=1
        self.hobby=[]
    def attack(self,enemy):   #普通攻击技能，enemy是敌人;
        enemy.life_value-=self.aggressivity #根据自己的攻击力，攻击敌人就减掉敌人的生命值。

# g1 = Garen('草丛伦')
# g2 = Garen('草丛伦2')
# g3 = Garen('草丛伦3')

# # print(g1.camp)
# # print(g2.camp)
# # Garen.camp=123
# # print(g3.camp)
# # print(g1.camp)
# # print(g2.camp)

# print(g1.hobby,id(g1.hobby))
# print(g2.hobby,id(g2.hobby))
# print(g3.hobby,id(g3.hobby))
# #
# # # g1.camp='123123123123'
# g1.hobby.append('g1 hobby')
# g2.hobby.append('g2 hobby')
# g3.hobby.append('g3 hobby')
# print(g1.hobby)

# # g1.camp='123123123123'
# # print(g1.camp)
# # print(g2.camp)
# # print(g3.camp)
#
# # print(g1.__dict__)
# print(g1.n)
# print(g3.n)
# print(Garen.n)


#类的函数是绑定到每个对象的，每个对象绑定方法都是不一样的，但都是同一种功能

class Garen:        #定义英雄盖伦的类，不同的玩家可以用它实例出自己英雄;
    camp='Demacia'  #所有玩家的英雄(盖伦)的阵营都是Demacia;
    n=0
    # hobby=[]
    def __init__(self,nickname,aggressivity=58,life_value=455): #英雄的初始攻击力58...;
        self.nickname=nickname  #为自己的盖伦起个别名;
        self.aggressivity=aggressivity #英雄都有自己的攻击力;
        self.life_value=life_value #英雄都有自己的生命值;
        Garen.n+=1
        self.hobby=[]
    def attack(self,enemy):   #普通攻击技能，enemy是敌人;
        print('=====>',self)
        print('=====>',enemy)
        # enemy.life_value-=self.aggressivity #根据自己的攻击力，攻击敌人就减掉敌人的生命值。

g1 = Garen('草丛伦')
# print(g1.attack)
# print(Garen.attack)

# g1.attack(g1) #Garen.attack(g1,g1)
#







