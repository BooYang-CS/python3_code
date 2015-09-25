print(abs(-100))
print(max(2,5,6,11))
print(int('123'))
print(int(12.44))
print(float('12.56'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(0))
print(bool(''))
#函数名其实就是一个指向一个函数对象的引用，完全可以把函数名赋给另一个变量，相当于给函数起了一个别名
a=abs
print(a(-200))
print(hex(255))#hex()将一个整数转换成十六进制表示的字符串
#函数定义
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-200))
#空函数,pass可以作为占位符，比如现在还没有想好怎么写函数的代码，一个pass可以让代码先运行起来
def nop():
	pass
#参数不对会抛出TypeError。
#print(abs('A'))#参数不对，内置abs会检查参数错误，自定义的my_abs没有参数检查。
#print(my_abs("A"))
def my_abs1(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs1(-222))
#print(my_abs1('aaa'))
#函数可以返回多个值
import math#表示导入math包，并允许后续代码引用math包的sin，con函数
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
r=move(100,100,60,math.pi/6)
print(r)
#函数返回值其实是一个元组tuple，元组是不能改变的，函数返回多个值其实就是返回一个tuple。
#函数练习
import math
def quadratic(a,b,c):
	if (b*b-4*a*c)>=0:
		n1=(-b+math.sqrt(b*b-4*a*c))/2*a
		n2=(-b-math.sqrt(b*b-4*a*c))/2*a
		return n1,n2
	else:
		return -1,-1
x,y=quadratic(1,-4,4)
print(x,y)