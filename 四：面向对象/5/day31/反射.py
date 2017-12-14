class People:
    country='China'
    def __init__(self,name):
        self.name=name
    # def walk(self):
    #     print('%s is walking' %self.name)
p=People('egon')
#
# People.country
# print(People.__dict__)

# print(p.name)
# print(p.__dict__)

# p.name


#hasattr
# print('name' in p.__dict__)
# print(hasattr(p,'name'))
# print(hasattr(p,'name1213'))

# print(hasattr(p,'country')) #p.country
# print(hasattr(People,'country')) #People.country
# print(hasattr(People,'__init__')) #People.__init__


#getattr
# res=getattr(p,'country') #res=p.country
# print(res)
#
# f=getattr(p,'walk') #t=p.walk
# print(f)
#
# f1=getattr(People,'walk')
# print(f1)
#
# f()
# f1(p)


# print(p.xxxxxxx)
# print(getattr(p,'xxxxxxxx','这个属性确实不存在'))

#
# if hasattr(p,'walk'):
#     func=getattr(p,'walk')
#     func()
#
# print('================>')
# print('================>')


#setattr

# p.sex='male'
# print(p.sex)
# print(p.__dict__)

# setattr(p,'age',18)
# print(p.__dict__)
# print(p.age)
# print(getattr(p,'age'))










#delattr
# print(p.__dict__)
# del p.name
# print(p.__dict__)

print(p.__dict__)
delattr(p,'name')
print(p.__dict__)













