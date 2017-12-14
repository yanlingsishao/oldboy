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
        People.__init__(self,name,sex,age)
        self.language=language

    def walk(self):
        People.walk(self)
        print('====>')

class North_korean(People):
    country='Korean'


c=Chinese('egon','male',18)
# print(c.name,c.age,c.sex)

print(c.__dict__)
print(c.country)


c.walk()



