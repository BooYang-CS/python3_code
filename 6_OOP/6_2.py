#类和实例
'''
class Student(object):
	pass
class 后是类名，即Student，类名通常是大写开头的单词，紧接着是（object）,表示
该类是从哪个类继承下来的，如果没有合适的继承类，就使用object类，这是所有的类都会继承的类。
'''
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
'''
在创建实例时，把一些必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法，在创建
实例时，把name和score等属性绑上去。
__init__方法的第一个参数永远是self，表示创建的实例本身，在__init__方法内部，就可以把各种属性绑定到
self,因为self就指向创建的实例本身。
有了__init__方法，在创建实例时，就不能传入空参数，必须传入与__init__方法匹配的参数。
但self不需要传。
'''
bart=Student('Bart Simpson',30)
print(bart.name)
print(bart.score)

#数据封装，将访问实例对象的函数和类关联起来实现数据封装。可以给类增加新的方法。
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s' % (self.name,self.score))
	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'
bart1=Student('lili',94)
bart1.print_score()
print(bart1.get_grade())
'''
类是创建实例的模板，而实例则是一个个具体的对象，各个实例拥有的数据都互相独立，互不
影响，方法是与实例绑定的函数，可以直接访问实例的数据。
python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然他们都是同一个类的
不同实例，但拥有的变量名称都可能不同
'''
bart2=Student('youyo',89)
lisa=Student('yiyi',81)
bart2.age=8#绑定一个名为age的数据。
print(bart2.age)
#print(lisa.age)#实例lisa没有绑定age数据，会报错

#访问限制
#从Student类的定义来看，外部代码还是可以自由修改一个实例的name和score属性
bart3=Student('popo',89)
print(bart3.score)
bart3.score=81
print(bart3.score)
"""
如果要让内部属性不被外部访问，可以把属性的名称前面加上两个下划线__,在python中，实例的
变量名如果以__开头，就变成了一个私有变量，只允许内部访问，不允许外部访问
"""
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s:%s' % (self.__name,self.__score))
bart4=Student('Bart lili',67)
#print(bart4.__name)#无法从外部访问实例变量.__name和实例变量.__score
'''
如果外部代码要获取name和score，可以给Student类增加get_name和get_score方法,又要允许外部代码修改score，
可以给Student类增加set_score方法.
'''
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s:%s' % (self.__name,self.__score))
	def get_name(self):#允许外部代码访问
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):#允许外部代码修改属性，引入此方法可以对参数做检查，避免传入无效参数
		self.__score=score
	def set_score1(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
bart5=Student('gaoxin',81)
print(bart5.get_score())
print(bart5.get_name())
bart5.set_score(90)
print(bart5.get_score())
bart5.set_score1(99)
print(bart5.get_score())
#bart5.set_score1(111)
'''
在python中，变量名类似__XXX__的，以双下划线开头和结尾的是特殊变量，特殊变量可以直接访问，不是private变量
但看到一单下划线开头的实例变量名_xxx,这样的实例变量名外部可以访问，但是按照约定，这样的变量可以访问，但是
将其视为私有变量，不要随意访问。
以双下划线开头的实例变量是不是一定不能从外部访问，其实也不是，不能访问是因为python解释器对外把__name变量
改成了_Student__name，所以可以通过_Student__name来访问__name变量，但强烈不建议这么做，因为不同版本的python解释器
会把__name改成不同的变量名。
'''
print(bart5._Student__name)
