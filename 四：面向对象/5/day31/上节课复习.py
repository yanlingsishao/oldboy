# # class Foo:
# #     def __init__(self):
# #         self.test=123
# #     @property
# #     def test(self):
# #         print('from test')
# #
# #     @test.setter
# #     def test(self,value):
# #         print('from test setter',value)
# #
# #
# #     @test.deleter
# #     def test(self):
# #         print('from test deleter')
# # f=Foo()
# # f.test
# # del f.test
#
#
# class People:
#     def __init__(self,name,x):
#         self.name=name
#         self.__SEX=x
#
#     @property
#     def sex(self):
#         return self.__SEX #self._People__SEX
#
#     @sex.setter
#     def sex(self,value):
#         if not isinstance(value,str):
#             raise TypeError('must be str')
#         self.__SEX=value
#
#     @sex.deleter
#     def sex(self):
#         raise Exception('不让删除')
#         # del self.__SEX
#
# p=People('egon','male')
# # print(p.sex)
# #
# # p.sex='female'
# # print(p.sex)
# # del p.sex
# # print(p.sex)
#
# # p.sex=123
# # del p.sex
#
#
#
# class People:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#     @property
#     def bodyindex(self):
#         return self.weight/(self.height**2)
#
#
# p=People('egon',18,1.80,90)
# print(p.bodyindex)
# p.height=1.85
# print(p.bodyindex)
























class Foo:
    def test1():
        print('test1')

    def test2(self):
        print('test2',self)

    def test3(self):
        pass

    @classmethod
    def test4(cls,x):
        print('classmethod test4',cls,x)


    @staticmethod
    def test5(x):
        print('staticmethod test5',x)


    def test6():
        print('test6')
# print(Foo.test1)
# print(Foo.test2)


f1=Foo()

# print(f1.test1)
# print(f1.test2)
#
# # f1.test1()
#
# f1.test2()
#
# Foo.test4(1)
#
# f1.test4(2)



Foo.test5(1)
f1.test5(2)


