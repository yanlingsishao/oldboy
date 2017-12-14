class People:
    def __init__(self,name):
        self.name=name


p=People('egon')


# print(type(p))
#
# print(type(People))

#typer--->类------>对象



class Foo:
    x=1
    def run(self):
        pass
print(type(Foo))



#type成为元类，是所有类的类，利用type模拟class关键字的创建类的过程
def run(self):
    print('%s is runing' %self.name)

class_name='Bar'
bases=(object,)
class_dic={
    'x':1,
    'run':run
}

Bar=type(class_name,bases,class_dic)
print(Bar)
print(type(Bar))


