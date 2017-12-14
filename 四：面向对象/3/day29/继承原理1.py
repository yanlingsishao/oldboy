#新式类的继承，在查找属性时遵循：广度优先
class A(object):
    def test(self):
        print('from A')
    pass
class X(A):
    # def test(self):
    #     print('from X')
    pass
class B(X):
    # def test(self):
    #     print('from B')
    pass
class C(A):
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
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()


#广度优先：F->D->B->E->C->A->object