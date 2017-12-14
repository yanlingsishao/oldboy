#多态：同一种事物的多种形态，动物分为人类，猪类（在定义角度）
class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')


class People(Animal):
    def run(self):
        print('人正在走')

class Pig(Animal):
    def run(self):
        print('pig is walking')


class Dog(Animal):
    def run(self):
        print('dog is running')

peo1=People()
pig1=Pig()
d1=Dog()

peo1.run()
pig1.run()
d1.run()



#多态性：一种调用方式，不同的执行效果（多态性）
def func(obj):
    obj.run()

func(peo1)
func(pig1)
func(d1)


# peo1.run()
# pig1.run()


# 多态性依赖于：
#     1.继承
#     2.
##多态性：定义统一的接口，
def func(obj): #obj这个参数没有类型限制，可以传入不同类型的值
    obj.run() #调用的逻辑都一样，执行的结果却不一样


func(peo1)
func(pig1)

func(d1)