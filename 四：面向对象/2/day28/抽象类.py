import abc
#抽象类：本质还是类，与普通类额外的特点的是：加了装饰器的函数，子类必须实现他们
class Animal(metaclass=abc.ABCMeta):
    tag='123123123123123'
    @abc.abstractmethod
    def run(self):
        pass
    @abc.abstractmethod
    def speak(self):
        pass



class People(Animal):
    def run(self):
        pass

    def speak(self):
        pass


peo1=People()
print(peo1.tag)
