# import sys
# from functools import wraps
#
# debug_log = sys.stderr
#
#
# def my_decorator(func):
# 	@wraps(func)
# 	def wrapper(*args, **kwargs):
# 		debug_log.write('Function：%s\n'% (func.__name__))
# 		debug_log.write('Parameter：%s\n'% (str(args)))
# 		res = func(*args, **kwargs)
# 		debug_log.write('Return value:{}\n'.format(res))
# 		return res
#
# 	return wrapper
#
#
# @my_decorator
# def add(x):
# 	return x + x
#
# @my_decorator
# def square(x,y):
# 	return x * y
#
# if __name__ == '__main__':
# 	add(3)
# 	#square(3,4)
x = ("1")
print(type(x))