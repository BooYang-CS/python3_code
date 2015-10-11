#1. 多重继承
#大类
class Animal(object):
	pass
#鸟类和哺乳类
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
#各种动物
class Dog(Mammal):
	pass
class Bat(Mammal):
	pass
class Parrot(Bird):
	pass
class Ostrich(Bird):
	pass
#给各种动物加上Runnable和Flyable的功能
class Runnable(object):
	def run(self):
		print('Running....')
class Flyable(object):
	def fly(self):
		print("Flying....")
#对需要Runnable功能的动物，就多继承一个Runnable
class Dog(Mammal,Runnable):
	pass
#对需要Flyable功能的动物，就多吉成一个Flyable
class Bat(Mammal,Flyable):
	pass
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
d=Dog()
d.run()
'''
在设计类的继承关系时，主线都是单一继承下来的，但是，如果需要增加额外的功能，通过多重继承就
可以实现。这种设计通常称之为MixIn.
MixIn的目的就是给一个类增加多个功能，在设计类的时候，优先考虑通过多重继承来组合多个MixIn的
功能，而不是设计多层次的复杂的继承关系。
'''
#为了更好的看出继承关系，可以把Runnable改成RunnableMixIn,以便不会产生同名错误。
#class Dog(Mammal,RunnableMixIn):
#	pass

#2. 定制类
#Python的class中还有很多这样有特殊用途的函数，可以帮助我们定制类
#2.1__str__特殊变量
class Student(object):
	def __init__(self,name):
		self.name=name
print(Student('bibi'))#结果是一个函数的地址,但是我们需要返回一个字符串
#这里就需要定义好__str__()方法了
class Student2(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student2 object (name:%s)' % self.name
print(Student2('Bobo'))
s=Student2('Wenwen')
print(s)
'''
在交互模式下，直接输入变量名s的结果和打印s的结果不一样.因为直接显示变量调用的不是__str__(),
而是__repr__(),两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的
字符串，也就是说，__repr__()是为调试服务的。解决方法就是再定义一个__repr__()。通常__str__()
和__repr__()代码都是一样的。
'''
class Student3(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student3 object (name=%s)' % self.name
	__repr__=__str__
print(Student3('dada'))
s1=Student3("jieya")
print(s1)
#2.2 __iter__
'''
如果一个类想被用于for...in循环，类似list或者tuple，就必须实现一个__iter__方法，该方法返回一个迭代
对象，然后后python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到
StopIteration错误时推出循环。
'''
class Fib(object):
	def __init__(self):
		self.a,self.b=0,1#初始化两个计数器
	def __iter__(self):
		return self #实例本身就是迭代对象，返回自己
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>10000:#退出循环条件
			raise StopIteration
		return self.a#返回下一个值
#把Fib实例用于for循环
f=Fib()
for n in f:
	print(n)
#2.3 __getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是把它当成list使用还是不行的，比如取地5个元素
#print(Fib()[5])#还不能像list一样使用
#要使得类的对象实例像list一样使用，需要__getitem__()方法
class Fib1(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
f1=Fib1()
print(f1[1])#可以按下标数列访问任意一项了
#但是list的切片方法却还不能使用
print(list(range(100))[5:10])
#但是Fib却报错，原因是__getitem__()传入参数可能是一个int,也可能是一个切片对象slice,要做出判断
class Fib2(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L
f2=Fib2()
print(f2[1:5])
print(f2[:10])
print(f2[0:10])
'''
如果把对象看成dict，__getitem__()的参数也可能是一个可以作为key的object,与之对应的是__setitem__()方法
把对象视作list或者dict来对集合赋值，最后还有一个__delitem__()方法，用于删除某个元素
通过上面方法，我们自己定义的类表现得和python自带的list，tuple,dict没有区别，这完全归功于动态语言的
鸭子类型，不需要强制继承某个接口.
'''
#2.4 __getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
class Student(object):
	def __init__(self):
		self.name='Mary'
s=Student()
print(s.name)
'''
print(s.score)#会报错，为了避免这个错误，除了加上一个score属性，python还有另一个机制，那就是
写一个__getattr__()方法,动态返回一个属性。
'''
class Student1(object):
	def __init__(self):
		self.name='BOBI'
	def __getattr__(self,attr):
		if attr=='score':
			return 404
			#return lambda:25
#当调用不存在的属性时，python解释器会试图调用__getattr__(self,'score')来尝试获得属性
s1=Student1()
print(s1.name)
print(s1.score)#返回一个自定义的数字，也可以返回一个函数
print(s1.age)#当没有这个属性时会返回一个None
'''
只有在没有找到属性的情况下，才调用__getattr__,已有的属性，比如name,不会在__getattr__中查找。
注意到任意调用如s1.age都会返回None,因为我们定义的__getattr__默认返回的就是None.
要让class只响应特定的几个属性，按照约定，抛出AttributeError的错误
'''
class Student2(object):
	def __getattr__(self,attr):
		if attr=='age':
			return lambda:27
		raise AttributeError('\'Student2\' object has no attribute\'%s\'' % attr )
#这样把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊的手段

#2.5 __call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，用instance.method()来调用。
#也可以直接在实例本身上调用。
#任何一个类，只要定义了一个__call__方法，就可以直接对实例进行调用
class Student3(object):
	def __init__(self,name):#注意Student1和Student3类参数不同，实例化的时候也不同
		self.name=name
	def __call__(self):
		print('My name is %s。' % self.name)
s3=Student3('lijie')
s3()#对实例进行直接调用
#__call__()还可以定义参数，对实例进行直接调用就好比对一个函数进行调用一样，可以把函数看成对象，也可以把对象看成函数
#能被调用的对象就是一个Callable对象，比如上面定义有__call__()的类实例
print(callable(Student()))
print(callable(s3))#Student3类实例必须进行初始化
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))
