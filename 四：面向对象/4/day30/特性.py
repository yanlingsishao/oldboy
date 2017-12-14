# import math
# class Circle:
#     def __init__(self,radius): #圆的半径radius
#         self.radius=radius
#
#     @property  #area=property(area)
#     def area(self):
#         return math.pi * self.radius**2 #计算面积
#
#     @property
#     def perimeter(self):
#         return 2*math.pi*self.radius #计算周长
#
#
#
#
#
#
# c=Circle(7)
# print(c.radius)
# c.radius=10
#
# # print(c.area())
# # print(c.perimeter())
# print(c.area)
# print(c.perimeter)



class People:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    @property
    def bodyindex(self):
        return self.weight/(self.height**2)


# p1=People('cobila',38,1.65,74)
# print(p1.bodyindex)
# p1.weight=200
# print(p1.bodyindex)



#被property装饰的属性会优先于对象的属性被使用

#而被propery装饰的属性,如sex,分成三种：
    # 1.property
    # 2.sex.setter
    # 3.sex.deleter

#
# class People:
#     def __init__(self,name,SEX):
#         self.name=name
#         # self.__sex=SEX
#         self.sex=SEX #self.sex='male'   p1.sex='male'
#     @property
#     def sex(self):
#         return self.__sex #p1.__sex
#
#     @sex.setter
#     def sex(self,value):
#         # print(self,value)
#         if not isinstance(value,str):
#             raise TypeError('性别必须是字符串类型')
#         self.__sex=value  #p1.__sex='male'
#     @sex.deleter
#     def sex(self):
#         del self.__sex #del p1.__sex


# p1=People('cobila','male')
# print(p1.tell_name())
#
# print(p1.sex)
# p1.sex='123'

# p1.sex='female'
# print(p1.sex)


# p1.sex=123123123123123123123123123213


# p1=People('cobila',123123123123123)
# p1=People('cobila','male')
# print(p1.sex)
# del p1.sex #del self.sex
# print(p1.sex)







































class People:
    def __init__(self,name,SEX):
        self.name=name
        # self.__sex=SEX
        self.sex=SEX#p1.sex='male'

    @property
    def sex(self):
        print('------proerty---------------------->')
        return self.__sex

    @sex.setter
    def sex(self,value):
        print('===================》')
        # print(self,value)
        # if not isinstance(value,str):
        #     raise TypeError('性别必须是字符串类型')
        self.__sex=value  #p1.ABCDEFG='male'
    @sex.deleter
    def sex(self):
        print('delete 操作')
        del self.__sex


p1=People('egon','male')
# print(p1.__dict__)
# print(p1.sex)
# del p1.sex
# print(p1.sex)

# print(p1.ABCDEFG)
# p1.ABCDEFG=123123
# print(p1.ABCDEFG)

# p1.sex
# print(p1.__dict__)


# p1.sex

# p1.sex='mall'

# del p1.sex







