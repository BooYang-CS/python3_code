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
print(lisa.age)#实例lisa没有绑定age数据，会报错