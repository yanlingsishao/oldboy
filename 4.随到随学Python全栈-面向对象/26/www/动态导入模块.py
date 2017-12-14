
# module_t=__import__('m1.t')
# print(module_t)
# # module_t.t.test1()
# # from m1.t import *
# # from m1.t import test1,_test2
# #
# # test1()
# # _test2()
# import  importlib
# m=importlib.import_module('m1.t')
# print(m)
# m.test1()
# m._test2()

moudule_t = __import__("m2.s1.x")
print(moudule_t)

import importlib
m = importlib.import_module('m2.s1.x')
print(m)