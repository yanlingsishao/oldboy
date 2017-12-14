# from collections import Iterable,Iterator
# class Foo:
#     def __init__(self,start):
#         self.start=start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return 'aSB'
#
#
# f=Foo(0)
# f.__iter__()
# f.__next__()

# print(isinstance(f,Iterable))
# print(isinstance(f,Iterator))
#
# print(next(f)) #f.__next__()
# print(next(f)) #f.__next__()
# print(next(f)) #f.__next__()


# for i in f: # res=f.__iter__() #next(res)
#     print(i)








# from collections import Iterable,Iterator
# class Foo:
#     def __init__(self,start):
#         self.start=start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > 10:
#             raise StopIteration
#         n=self.start
#         self.start+=1
#         return n
#

# f=Foo(0)


# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#
# for i in f:
#     print('====>',i)




# class Range:
#     '123'
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#         n=self.start
#         self.start+=1
#         return n
#
# for i in Range(0,3):
#     print(i)
#
#
#
# print(Range.__doc__)


class Foo:
    '我是描述信息'
    pass

class Bar(Foo):
    pass
print(Bar.__doc__) #该属性无法继承给子类

b=Bar()
print(b.__class__)
print(b.__module__)
print(Foo.__module__)
print(Foo.__class__) #?

