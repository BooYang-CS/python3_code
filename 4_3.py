#排序算法
#python内置sorted()函数就可以对list进行排序
print(sorted([23,5,-3,51,7,8]))
#sorted()也是一个高阶函数，可以接收一个可以函数实现自定义排序
print(sorted([1,5,3,-2,0,-23,9],key=abs))
#字符串排序
print(sorted(['bob','hude','sdsd','addc']))#按照ascii的大小比较
print(sorted(['BUd','Buas','aad','Add'],key=str.lower))#实现字符串，忽略大小写排序，str.lower表示按小写排序
print(sorted(['BUd','Buas','aad','Add'],key=str.lower,reverse=True))#将结果实现反向排序，传入第三个参数就可以了
'''
练习1：用tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
用sorted()对上述列表分别按名字排序
'''
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
	return t[0]
L1=sorted(L,key=by_name)#列表list L中的元素是一个tuple，t[0]表示tuple的第一个元素
print(L1)
'''
练习2：用tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
用sorted()对上述列表分别按成绩排序
'''
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
	return t[1]
L1=sorted(L,key=by_name,reverse=True)#列表list L中的元素是一个tuple，t[0]表示tuple的第一个元素
print(L1)

'''
函数作为返回值，高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
'''
#先实现一个可变参数的求和函数
def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax
#如果不需要立即求和，而是在后面的代码中，根据需要在计算，可以不返回求和结果，而是返回求和函数
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
f=lazy_sum(1,2,3,4,5)#因为参数是可变参数，即参数的个数可变，不用组装成list或者tuple
print(f)#函数返回的并不是求和结果，而是求和函数的地址
print(f())#等真正调用函数f()使，才返回求和结果
'''
函数lazy_sum中又定义了函数sum,内部函数sum可以引用外部函数lazy_sum的参数和局部
变量，当lazy_sum返回函数sum时，相关的参数和变量都保存在返回的函数中，sum函数的返回
值就是求和结果。
'''
f1=lazy_sum(1,2,3,4,5)
f2=lazy_sum(1,2,3,4,5)
print(f1==f2)
#当调用lazy_sum函数，每次调用都会返回一个新的函数，即使传入相同的参数，f1和f2的调用结果互不影响
#返回函数并没有立即执行，直到调用f()才执行。
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f(i))
	return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
'''
在上面例子中，每次循环，都创建了一个新的函数，然后把创建的3个函数都返回了。
f1(),f2(),f3()的结果应该是1，4，9但实际都是9，原因在于返回的函数引用了变量i
但它并非立刻执行，等到3个函数都返回时，也就是调用f1()时，即执行i*i时，这时
i已经变成了3.
'''
#返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
#每次循环都创建了一个新的函数，然后把3个创建的函数都返回了，即在循环的过程中调用执行了函数f()

