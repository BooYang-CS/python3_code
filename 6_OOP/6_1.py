'''
面向对象编程
'''
#面向过程编程
std1={'name':'bobo','score':90}
std2={'name':'lili','score':89}
def print_score(std):
	print('%s:%s' % (std['name'],std['score']))
print_score(std1)
print_score(std2)
#面向过程编程
'''
将学生这种数据类型视为一个对象，对象拥有name和score这两个属性，如果要打印这个学生的成绩，
必须先创建这个学生对应的对象，然后，给对象发一个print_socre的消息，让对象自己把自己打印出来。
'''
class Student(object):
	def __init__(self,name,score):#self 表示对象本身，name和score是对象的两个属性
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s' % (self.name,self.score))
bart=Student('Bart Simpson',68)
lisa=Student('Lisa Simpson',89)#创建两个对象实例，并初始化
bart.print_score()
lisa.print_score()
#类和实例，面向对象的是设计思想就是抽象出class，根据class创建实例（instance）。
#面向对象的抽象程度又比函数要高，因为一个类class即包含数据，有包含操作数据的方法。