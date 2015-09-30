'''
匿名函数：在传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
'''
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,9])))#map函数返回的是一个Iterator，需要用list作为结果返回
#实际上匿名函数lambda x:x*x实际上就是
def f(x):
	return x*x
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
#匿名函数没有名字，不担心函数冲突，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量调用该函数
f=lambda x:x*x
print(f(5))
print(f)
#也可以把匿名函数作为返回值返回
def build(x,y):
	return lambda:x*x+y*y
print(build(2,3))#结果还是一个函数，<function build.<locals>.<lambda> at 0x0102DC00>
print(build(2,3)())#再次调用函数才能得到结果。
'''
装饰器：由于函数也是一个对象，而且函数对象也可以被赋值给变量，通过变量
也能调用该函数.
'''
def now():
	print('2015-09-25')
f=now
print(f())
#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
'''
现在需要增强now()函数的功能，比如，在函数调用后自动打印日志，但又不希望修改now()函数的功能，比如，在函数调用后自动打印日志，但又不希望now()函数 
的定义，这种在代码运行期间动态增加功能的方式，，称之为'装饰器'（Decorator）
'''
def log(func):
	def wrapper(*args,**kw): #可变参数和关键字参数
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
#log是一个装饰器，接受一个返回函数作为参数，并返回一个函数，借助python的@语法，把decorator置于函数定义处
@log
def now():
	print("2015-09-27")
now()
print(now.__name__)
'''
把@log放到now()函数定义处，相当于执行语句：now=log(now),原来的now函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新的函数。即log()函数中返回
的wrapper()函数。 
wrapper()函数的参数定义为(*args,**kw),因此wrapper()函数可以接受任意参数的调用。
'''
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2015-03-25')
now()
print(now.__name__)#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
#decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
#和2层嵌套的decorator相比，3层嵌套的效果是这样的：now=log('execute')(now)
#需要把原始函数的__name__等属性复制到wrapper()函数中，否则以来函数签名的代码执行就会出错
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('20150930')
now()
print(now.__name__)
#或者
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'% (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2015-09-30')
now()
print(now.__name__)
'''
练习：编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志,并且即支持
不带参数和带参数打印
'''
import functools
def log(arg):
	text='' if hasattr(arg,'__call__') else arg#判断arg是否具有某种对象属性
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call %s %s():' % (text,func.__name__))
			ret=func(*args,**kw)#调用原函数
			print('end call %s %s():' % (text,func.__name__))
			return ret
		return wrapper
	return decorator(arg) if hasattr(arg,'__call__') else decorator
@log
def now1():
	print('2015-09-30')
now1()
print(now1.__name__)
@log('execute')
def now2():
	print('2015-09-30')
now2()
print(now2.__name__)
#方法2
import functools
def log(text=''):#使用默认参数
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call %s %s():' % (text,func.__name__))
			ret=func(*args,**kw)#调用原函数
			print('end call %s %s():' % (text,func.__name__))
			return ret
		return wrapper
	return decorator
@log()#两则之间区别
def now1():
	print('2015-09-30')
now1()
print(now1.__name__)
@log('execute')
def now2():
	print('2015-09-30')
now2()
print(now2.__name__)