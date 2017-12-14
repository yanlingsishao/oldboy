class People:
    def __init__(self,name):
        self.name=name
    #
    def __call__(self, *args, **kwargs):
        print('call')
    #

p=People('egon')
print(callable(People))
print(callable(p))

p()