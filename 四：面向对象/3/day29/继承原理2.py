#新式类的继承，在查找属性时遵循：广度优先
class X(object):
    # def test(self):
    #     print('from X')
    pass
class Y(object):
    # def test(self):
    #     print('from Y')
    pass

class B(X):
    # def test(self):
    #     print('from B')
    pass
class C(Y):
    # def test(self):
    #     print('from C')
    pass
class D(B):
    # def test(self):
    #     print('from D')
    pass

class E(C):
    # def test(self):
    #     print('from E')
    pass
class F(D,E):
#     def test(self):
#         print('from F')
    pass
f1=F()
f1.test()


#F--->D---->B--->X--->E---->C---->Y---->object
