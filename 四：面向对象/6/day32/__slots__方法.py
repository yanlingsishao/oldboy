# class People:
#     x=1
#     def __init__(self,name):
#         self.name=name
#     def run(self):
#         pass
#
#
# print(People.__dict__)
#
# p=People('alex')
# print(p.__dict__)



class People:
    __slots__=['x','y','z']

p=People()
print(People.__dict__)

p.x=1
p.y=2
p.z=3
print(p.x,p.y,p.z)
# print(p.__dict__)

p1=People()
p1.x=10
p1.y=20
p1.z=30
print(p1.x,p1.y,p1.z)
print(p1.__dict__)
