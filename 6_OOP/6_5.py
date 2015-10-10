#1.使用__slots__
'''
正常情况下，创建一个class实例后，可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
'''
class Student(object):
	pass
s=Student()
s.name='bobo'#动态给实例绑定一个属性
print(s.name)
#还可以尝试给实例绑定一个方法
def set_age(self,age):
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
s.set_age(23)
print(s.age)
#但是给一个实例s绑定方法，对另一个实例s1是不起作用的
s2=Student()
#s2.set_age(26)#会报错
#要给所有的实例都绑定方法，可以给class绑定方法
def set_score(self,score):#绑定一个方法的同时，该实例或则对象就拥有属性score了
	self.score=score
Student.set_score=MethodType(set_score,Student)#给class绑定一个方法，所有的实例都可以调用
s.set_score(100)
print(s.score)
s2.set_score(88)
print(s2.score)
#通常情况下可以在class中直接定义方法，但是动态绑定可以在程序运行时给class增加功能。
'''
如果要限制实例的属性，例如只允许对Student实例添加name和age属性。为了达到限制的目的，python允许
在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。
'''
class Student1(object):
	__slots__=('name','age')#用tuple定义允许绑定的属性的名称
s1=Student1()
s1.name='lili'
s1.age=34
#s1.score=88#绑定属性score失败
#使用__slots__要注意，__slots__定义的属性仅对当前实例其作用，对继承的子类不起作用的
class GraduateStudent(Student1):
	pass
g=GraduateStudent()
g.score=98
print(g.score)
#子类没有父类的属性限制，除非子类也定义__slots__,这样子类允许定义的属性就是自身的__slots__和父类的__slots__

#2. 使用@property
'''
在绑定属性时，如果直接把属性暴露出来，虽然写起来简单，但是没办法检查参数，导致可以随意修改属性值.
'''
#可以使用函数的方法来获取属性值和修改属性值并且检查参数
class Student2(object):
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value <0 or value >100:
			raise ValueError('score must between 0-100!')
		self._score=value
s4=Student2()
s4.set_score(87)
print(s4.get_score())
print(s4._score)
#s4.set_score(200)
#上述方法比较复杂，即能检查参数，又可以用类似属性这样简单的方法来访问类的变量
#python 内置的@property装饰器就可以把一个方法变成属性调用
class Student3(object):
	@property 
	def score(self):#这是一个getter方法
		return self._score
	@score.setter
	def score(self,value):#这是个setter方法
		if not isinstance(value,int):
			raise ValueError("score must be an integer!")
		if value<0 or value>100:
			raise ValueError("score must between 0~100")
		self._score=value
'''
把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter,
负责把一个setter方法变成属性值。
'''
s5=Student3()
s5.score=80
print(s5.score)
#s5.score=200

'''
比较Student2和Student3,了解@property 的用法。在对实例属性操作的时候，就知道该属性可能不是直接暴露的，
而是通过getter和setter方法来实现的
'''
#还可以定义只读属性，只定义getter方法，不定义setter方法
class Student4(object):
	@property 
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth=value
	@property 
	def age(self):
		return 2015-self._birth
#Student4中birth是一个可读写属性，age就只是一个只读属性。
s6=Student4()
s6.birth=1991
print(s6.birth)
#s6.age=20#age只是可读属性不能修改
print(s6.age)

'''
练习：利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
'''
class Screen(object):
	@property 
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width=value
	@property 
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height=value
	@property 
	def resolution(self):
		return self._height*self._width
t=Screen()
t.width=1024
t.height=768
print(t.resolution)