#高阶函数
print(abs(-100))
x=abs(-122)
print(x)
f=abs
print(f)#函数本身赋值给变量，变量可以指向函数
print(f(-111))#变量f已经指向abs函数本身
#函数名本身其实就是指向函数的变量
#abs=100
print(abs(-100))
#函数abs指向其他对象，就无法通过abs(-10)调用该函数。因为abs变量已经不指向求绝对值函数。
#要恢复abs()函数，请重启python交互环境。
#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x,y,f):
	return f(x)+f(y)
print(add(-11,-333,abs))
'''
map/reduce函数
map()函数接收两个参数，一个是函数，一个是Iterable(可以直接作用于for循环的对象)，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
	return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
'''
#方法1
for x in r:
	print(x)
'''
print("hello,world")
'''
#方法2
while True:
	try:
		print(next(r))
	except StopIteration:
		break;
'''
'''
方法1和方法2不能同时调用，因为r是属于Iterator,不断的调用next()函数按需计算系一个数据，当获得最后一个数据后，
会抛出StopIteration异常。如果再次调用next()函数，会不起作用
'''
print(list(map(str,[1,2,3,4,5,6,7])))
'''
reduce函数，reduce把一个函数作用在一个序列[x1,x2,x3,x4,..]上，这个函数必须接受两个参数，
reduce把结果继续和序列的下一个元素做累计计算，例如：
reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
'''
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,2,3,5,7]))#求和运算

from functools import reduce 
def fn(x,y):
	return x*10+y
print(reduce(fn,[1,2,3,4,5]))#将一个整数list，变成一个整数

from functools import reduce
def fn(x,y):
	return x*10+y
def char2nums(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[s]
print(reduce(fn,map(char2nums,'12345677')))#将字符串转换成整数

from functools import reduce 
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2nums(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[s]
	return reduce(fn,map(char2nums,s))
print(str2int('135465654665'))#将字符串转换成整数

'''
练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
输入：['adam','LISA','BarT'],输出：['Adam','Lisa','Bart']
'''
def normalize(name):
	return str(name).capitalize()#capitalize()函数是将字符串首字母大写，其他小写的函数
L1=['adam','LISA','BarT']
L2=list(map(normalize,L1))
print(L2)#方法1
def normalize(name):
	return name[0].upper()+name[1:].lower()
L1=['adam','LISA','BarT']
L2=list(map(normalize,L1))
print(L2)#方法2
'''
练习2：python提供的sum()函数可以接收一个list并求和，请编写一个prod()函数，
可以接受一个list并利用reduce()求积
'''
from functools import reduce
def prod(L):
	return reduce(lambda x,y:x*y,L)
L=[3,4,5,6]
print('3*4*5*6=',prod(L))