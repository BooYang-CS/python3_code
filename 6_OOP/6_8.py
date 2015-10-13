#深入理解python中的元类(metaclass)
class ObjectCreator(object):
	pass
my_object=ObjectCreator()
print(my_object)
#这个对象（类）自身拥有创建对象（类实例)的能力，这就是为什么它是一个类的原因
print(ObjectCreator)#可以打印一个类，因为它其实就是一个对象

def echo(o):
	print(o)
echo(ObjectCreator)#可以将类作为参数传给函数

print(hasattr(ObjectCreator,'new_attribute'))#hasattr()函数判断类是否具有某种属性
ObjectCreator.new_attribute='foo'#直接给类增加属性
print(ObjectCreator.new_attribute)

ObjectCreatorMirror=ObjectCreator#可以将类赋值给一个变量
print(ObjectCreatorMirror)
print(ObjectCreatorMirror())

#类也是对象，可以在运行时动态的创建它们，就像其他任何对象一样。
def choose_class(name):
	if name=='foo':
		class Foo(object):
			pass
		return Foo#返回的是类，不是类的实例
	else:
		class Bar(object):
			pass
		return Bar
MyClass=choose_class('foo')
print(MyClass)#函数返回的是类，不是类的实例
print(MyClass())#可以通过函数返回的类来创建一个实例，也就是对象

#当使用class关键字时，python解释器自动创建这个对象。现在这个自动创建对象的交给自己来处理，python是允许这么做的。
#可以通过type()函数知道一个对象的类型是什么
print(type(1))
print(type('1'))
print(type(ObjectCreator))#类的类型还是类
print(type(ObjectCreator()))#实例的类型

#type()函数还有一个功能，它可以动态创建类。type可以接受一个类的描述作为参数，然后返回一个类

#type(类名，继承的父类集合(注意单个元组的表示方法)，包括属性或方法的字典dict)
#自动创建一个类
class MyShinyClass(object):
	pass
#手动创建
MyShinyClass1=type('MyShinyClass1',(),{})#返回一个类对象
print(MyShinyClass1)#返回一个类名
print(MyShinyClass1())#返回一个该类的实例

#type接受一个字典来为类定义属性

Foo=type('Foo',(),{'bar':True})#bar是类Foo的一个属性，其值为True
print(Foo)
f=Foo()
print(f.bar)

#等价于
'''
class Foo(object):
	bar=True
'''
#也可以向这个类继承
FooChild=type('FooChild',(Foo,),{})#注意单个元组的写法
#等价于
'''
class FooChild(Foo):
	pass
'''
f1=FooChild()
print(f1.bar)

#为类增加方法
def echo_bar(self):#该函数是调用对象自身的bar属性
	print(self.bar)
FooChild1=type('FooChild1',(Foo,),{'echo_bar':echo_bar})
print(hasattr(Foo,'echo_bar'))#Foo没改该方法
print(hasattr(FooChild1,'echo_bar'))
my_foo=FooChild1()
my_foo.echo_bar()

#使用关键字class时，python在幕后做的事情就是通过元类来实现的
#类是用来创建实例的，而元类就是用来创建类的。
'''
MyClass=Metaclass()
MyObject=MyClass()
#而type已经可以这样做了
MyClass=type('MyClass',(),{})
#所以type就是python背后用来创建所有类的元类，type是小写形式可能是为了和str,int保持一致。
#python中所有的东西都是对象，他们都是从一个类创建的。
'''
age=25
print(age.__class__)
name='bobo'
print(name.__class__)
def foo():
	pass
print(foo.__class__)
class Bar(object):
	pass
b=Bar()
print(b.__class__)
#可以通过__class__查看所属的类，__class__的__class__属性是什么,是元类
print(age.__class__.__class__)
print(foo.__class__.__class__)
print(b.__class__.__class__)

#在写一个类的时候为其添加__metaclass__属性，如果这样做了，python就会用元类来创建类
'''
class Foo(object):
	__metaclass__=something
'''
'''
当写下class Foo(object),但是类对象还没有在内存中创建，python会在类的定义中寻找__metaclass__属性，如果找到了，python会用它来创建
类，如果没有找到会用内建的type来创建这个类。
'''
#元类的主要目的是为了创建类时能够自动的改变类。当你需要在模块的所有的类都需要某种特殊的属性时，这时候就可以使用元类来创建类

def upper_attr(future_class_name,future_class_parents,future_class_attr):#返回一个类对象，将属性都转为大写形式
	#选择所有不以'__'开头的属性
	uppercase_attr={}#是一个dict字典
	for name,value in future_class_attr.items():
		if not name.startswith('__'):
			#将它们转换为大写形式
			uppercase_attr[name.upper()]=value
		else:
			uppercase_attr[name]=value
	return type(future_class_name,future_class_parents,uppercase_attr)#通过type来做类对象的创建
#__metaclass__=upper_attr#这会作用到这个模块中的所有类
class Foo3(metaclass=upper_attr):#我们也可以在这里定义__metaclass__,这样只会作用于这个类中
	bar='bip'
print(hasattr(Foo3,'bar'))#false
print(hasattr(Foo3,'BAR'))#True
f=Foo3()
print(f.BAR)

#现在用一个class来当作元类
#type实际上是一个类，就像'str'和'int'一样,所以可以从type继承
class UpperAttrMetaclass(type):
	#__new__是在__init__之前被调用的特殊方法
	#__new__是用来创建对象并返回之的方法，而__init__只是用来将传入参数初始化对象
	#创建的对象是类，我们希望能够自定义它，所以这里改写为__new__()
	def __new__(upperattr_metaclass,future_class_name,future_class_parents,future_class_attr):
		uppercase_attr={}
		for name,value in future_class_attr.items():
			if not name.startswith('__'):
				uppercase_attr[name.upper()]=value
			else:
				uppercase_attr[name]=value
		return type(future_class_name,future_class_parents,uppercase_attr)
#但是这种方式其实不是OOP.我们直接调用了type，而且没有改写父类的__new__方法。
class UpperAttrMetaclass1(type):
	def __new__(upperattr_metaclass,future_class_name,future_class_parents,future_class_attr):
		uppercase_attr={}
		for name,value in future_class_attr.items():
			if not name.startswith('__'):
				uppercase_attr[name.upper()]=value
			else:
				uppercase_attr[name]=value
		#复用__new__方法，这才是基本的OOP
		return type.__new__(upperattr_metaclass,future_class_name,future_class_parents,uppercase_attr)
#类方法的第一个参数表示当前的实例。在真实的产品中一个元类应该是这样的
class UpperAttrMetaclass2(type):
	def __new__(cls,clsname,bases,dct):
		uppercase_attr={}
		for name,value in dct.items():
			if not name.startswith('__'):
				uppercase_attr[name.upper()]=value
			else:
				uppercase_attr[name]=value
		return super(UpperAttrMetaclass2,cls).__new__(cls,clsname,bases,uppercase_attr)
'''
元类的作用：
1.拦截类的创建
2.修改类
3.返回修改之后的类
'''
class Foo4(metaclass=UpperAttrMetaclass2):
	bar='bip'
f2=Foo4()
print(hasattr(f2,'bar'))
print(hasattr(f2,'BAR'))
