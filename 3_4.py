'''
生成器:在python中，一边循环一边计算的机制成为生成器：generator
'''
#创建一个生成器很简单，只需要把一个列表生成式的[]改成()
L=[x*x for x in range(1,10) if x%2==0]
print(L)
g=(x*x for x in range(10))
print(g)
#L是一个list，g是一个generator，可以直接打印list的每一个元素，可以通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
#这种调用generator元素的方式还是很麻烦，没有更多的元素时，会抛出Stopinteration错误
#正确的方法是使用for循环，因为generator也是可迭代对象
from collections import Iterable
print(isinstance(g,Iterable))
r=(x*x for x in range(1,6) if x%2!=0)
for n in r:
	print(n)
#generator非常强大，当推算的算法比较复杂，用类似列表生成式的for无法实现时，可以用函数实现
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b;
		n=n+1
	return 'done'
print(fib(10))#斐波拉契数列的函数表达式
#上述函数，可以从第一个元素开始，推算出后续任意的元素，这种逻辑和generator非常相似
#只要将print(b)改成yield b就行了
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b;
		n=n+1
	return 'done'
print(fib(10))#这样就变成了一个生成器
'''
但是generator和函数的执行流程不一样，函数顺序执行，遇到return或者
最后一句就返回。而变成generator函数是在每次调用next()的时候执行，遇到
yield语句就返回，再次执行时下哦那个上次返回的yield语句出继续执行
'''
def odd():
	print("step 1")
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3
o=odd()
print(next(o))
print(next(o))
print(next(o))
#odd不是一个普通函数，而是generator，在执行过程中遇到yield就中断，下次又继续执行。
'''
fib函数改成generator后,用for循环调用generator时，发现拿不到generator的return
语句的返回值,要想得到返回值，必须捕获StopIteration错误，返回值包含在
StopIteration的value中
'''
for a in fib(5):
	print(a)
g=fib(10)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print("Generator return value:",e.value)
		break
'''
练习:杨辉三角，把每一行看成一个list，试写一个generator，不断输出下一行的list
'''
def triangles():
	L=[1]
	yield(L)
	L=[1,1]
	yield(L)
	while True:
		L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]#range是从0开始的
		yield(L)
n=1
o=triangles()
for t in o:
	print(t)
	n=n+1
	if n==10:
		break
#triangles()其实是一个generator，将杨辉三角的每一行当作一个list。
