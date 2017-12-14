#新式类的继承，在查找属性时遵循：广度优先
class A(object):
    def test(self):
        print('from A')
    pass

class B(A):
    # def test(self):
    #     print('from B')
    pass

class C(A):
    # def test(self):
    #     print('from C')
    pass

class D(A):
    # def test(self):
    #     print('from D')
    pass
class E(B):
    # def test(self):
    #     print('from E')
    pass
class F(C):
    # def test(self):
    #     print('from F')
    pass

class G(D):
    # def test(self):
    #     print('from G')
    pass

class H(E,F,G):
    # def test(self):
    #     print('from H')
    pass

h1=H()
h1.test()