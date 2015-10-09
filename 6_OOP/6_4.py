#获取对象信息，当拿到一个对象的引用时，如何知道这个对象的类型
#1.使用type()
#基本类型都可以用type()判断
print(type(123))
print(type('string'))
print(type(None))
#如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))
class Animal(object):
	pass
a=Animal()
print(type(a))
#type()函数返回类型。
print(type(123)==type(234))
print(type(123)==int)
print(type('123')==type('abd'))
print(type('abd')==str)
print(type('abc')==type(123))
#判断基本数据类型可以直接写int，str等。但是判断一个对象是否是函数，可以使用types模块中定义的常量
import types#导入types模块
def fn():#定义一个函数
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)
#2.使用isinstance()
#对于class的继承关系来说，使用type()很不方便，要判断class的类型使用isinstance()函数返回类型。
class Animal(object):
	def run(self):
		print('Animal is running....')
class Dog(Animal):
	pass
class Husky(Dog):
	pass
a=Animal()
d=Dog()
h=Husky()
print(isinstance(h,Husky))#没有问题，因为h变量就是指向Husky对象
print(isinstance(h,Dog))#h虽然是Husky类型，但是是从Dog继承下来的。所以h也是Dog类型
#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
print(isinstance(h,Animal))
#使用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))
#还可以判断一个变量是否是某些类型中的一种。
print(isinstance([12,3,4],(list,tuple)))
print(isinstance((12,3,4),(list,tuple)))
#3.使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list.
print(dir('asc'))
print(len('ADC'))#等价于
print('ADC'.__len__())
#用len()函数获取一个对象的长度，实际上在len()函数内部，它自动去调用该对象的__len__()方法
#自己写的类，如果也想用len(my_object)方法，可以在类内部写一个__len__()方法
class My_object(object):
	def __len__(self):
		return 1000
dog=My_object()
print(len(dog))#如果类不定义__len__()方法，在外部调用len()函数时，会出错。因为该对象没有__len__属性
#字符串的其他属性
print('ADC'.lower())#直接调用lower()方法，返回小写的字符串
#配合getattr(),setattr()和hasattr()可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x'))#测试对象obj有属性'x'吗
print(obj.x)
print(hasattr(obj,'y'))#现在测试对象obj没有属性'y'
setattr(obj,'y',20)#设置一个属性'y'
print(hasattr(obj,'y'))#再次测试是否有属性'y'
print(getattr(obj,'y'))#获取属性'y'
print(obj.y)
#试图获取不存在的属性，会抛出AttributeError的错误
#getattr(obj,'z')#获取属性'z'
#可以传入一个default参数，如果属性不存在，就返回默认值。
print(getattr(obj,'z',404))#如果'z'属性不存在，会返回一个默认值404
#也可以获得对象的方法，也就是对象定义的函数
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn=getattr(obj,'power')#获取属性'power',并赋值给变量fn
print(fn)
print(fn())
#只有在不知道对象信息的时候，我们才会去获取对象信息.

#实例属性和类属性
#由于python是动态语言，根据类创建的实例可以任意绑定属性
#给实例绑定属性的方法是通过实例变量或者self变量
class Student(object):
	def __init__(self,name):
		self.name=name
s=Student('Bob')
s.score=90#通过实例变量绑定属性，其中name和score都是实例属性
#但是，Student类本身需要绑定一个属性，可以直接在class中定义属性，这种属性是类属性
class Student(object):
	name='Student'
#虽然定义了一个类属性，这个属性归类所有，但是类的所有实例都可以访问到
s=Student()
print(s.name)#打印实例的name属性，但是实例并没有该属性，所以会继续查找class的name属性
print(Student.name)#打印类的name属性
s.name='BIHI'#给实例绑定name属性，之前没有
print(s.name)
print(Student.name)#但是类属性并没有消失
del s.name#删除实例的name属性
print(s.name)
'''
从上述例子可以看出，在编写程序时，别把实例属性和类属性使用相同的名字，因为相同名称
的实例属性会屏蔽掉类属性，当删除掉实例属性后，在使用相同的名字，访问到的将是类属性
'''