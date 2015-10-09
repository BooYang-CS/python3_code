#继承和多态
'''
在OOP程序设计中，当我们定义一个class时，可以从现有的class继承，新的class称为子类（Subclass）
而被继承的称为基类，父类或超类（Base class，Super class)
'''
class Animal(object):
	def run(self):
		print('Animal is running....')
class Dog(Animal):
	pass
class Cat(Animal):
	pass
#Animal是父类，Dog和Cat是其子类，子类可以获取父类的全部功能。
dog=Dog()
dog.run()#子类Dog继承了父类的run方法。
class Dog1(Animal):
	def run(self):#子类也可以增加一些方法
		print('Dog is running...')
	def eat(self):
		print('Eating meat....')
dog=Dog1()
dog.run()
dog.eat()
'''
当子类和父类都存在相同run()方法时，子类的run()覆盖了父类的run(),在代码运行时，
会调用子类的run(),这就是继承的另一好处，多态。
当定义一个class时，实际上就是定义了一种数据类型。
'''
a=list()#a 是list类型
b=Animal()#b 是Animal类型
c=Dog() #c 是Dog类型
print(isinstance(a,list))#判断变量是否是某个类型可以用isinstance()判断
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))#c不仅仅是Dog,还是Animal类型
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是反过来不行。
def run_twice(animal):#编写一个函数，接受一个Animal类型的变量
	animal.run()
run_twice(Animal())#以Animal类的实例作为函数参数
run_twice(Dog())
run_twice(Dog1())
#上述函数调用的run()函数都是子类的run函数
class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')
run_twice(Tortoise())
#新增一个Animal的子类Tortoise，不必对run_twice()做任何修改。
'''
继承可以把父类的所有功能都直接拿过来，这样不必重零做起，子类只需要新增自己特有的
方法，也可以把父类不适合的方法覆盖重写，这是多态。
'''