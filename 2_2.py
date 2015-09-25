#函数的参数
def power(x):
	return x*x
print(power(3))
def power(x,n=2):#默认参数，所以power函数的参数可以变化的
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print(power(3,4))
print(power(8))#修改power的参数后，继续使用原函数会报错，这时默认参数会解决此问题.
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
#使用默认参数可以降低调用函数的难度
def enroll(name,gender):
	print('name:',name)
	print('gender:',gender)
enroll('bobo','F')#直接调用函数输出几结果
print(enroll('bob','M'))#调用函数后，会打印函数的返回值为none
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enroll('boli','F')#age和city使用默认值
enroll('xiaoming','M',city='wuhan')#age继续使用默认值，city自定义
#使用默认参数注意事项,例如传入一个list，添加一个END后返回
def add_end(L=[]):
	L.append('END')
	return L
print(add_end([1,2,3]))#正常调用
print(add_end())#使用默认参数，结果为['END']
print(add_end())#再次调用，结果为['END','END']
#出现上述原因是函数在定义的时候，默认参数L的值就被计算出来了，即[],
#因为默认参数L也是一个变量，它指向对象[],每次调用该函数如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
#所以定义默认参数时必须指向不变对象
def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
print(add_end())
print(add_end())
#像str，None这样的不变对象，一旦创建，对象内部的数据就不能修改，可以减少修改数据导致的错误
#可变参数就是参数的个数是可以变的,如计算n组数字的平方和
#使用list或者tuple作为参数，参数就是一个元素，不可变
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
#可以将数字作为一个list或者tuple传进来
print(calc([1,2,3]))#list作为参数
print(calc((2,3,4,5,6)))#tuple作为参数
#如果利用可变参数，即参数的个数是可以变的
def calc1(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
print(calc1(1,2,3,4,5))#利用可变参数，调用方式可以简化
print(calc1())
#定义可变参数和定义一个list或tuple参数相比，仅在参数前面加了一个*号。
#如果已有了一个list或者tuple，要调用一个可变参数可以这样做
nums=[1,2,3,4]
print(calc(nums))#一个list参数
print(calc1(nums[0],nums[1],nums[2],nums[3]))#4个参数，可变参数
#但是上述写法太繁琐，Python允许在list和tuple前加一个*号，把list和tuple的元素变成可变参数传进去
print(calc1(*nums))#*nums表示把nums这个list的所有元素作为可变参数传进去在，这种写法相当有用，而且非常有用
#关键字参数
#可变参数允许传入0个或者人一个参数，这些参数在函数调用时自动组成一个tuple
#关键字参数允许你传入0个或者任意个参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传必选参数
print(person('mali',20))#函数返回值为空，打印出None
person('adam',45,gender='M',job='Engineer')
#关键字参数可以用来接收非必选参数外的数据
extra={'city':'Beijing','job':'Engineer'}#一个dict，将dict转换成关键字参数传出去
person('Jack',24,city=extra['city'],job=extra['job'])
person('Jack',24,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入函数的**kw参数，kw获得一个dict，注意kw获得的dict是extra的一个拷贝。对kw的改动不会影响到函数外的extra
#命名关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)
person("zhanzheng",23,city='Beijing',zpcode=1233)#限制关键字参数的名字，但上述函数仍不受限制的关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接受city和job作为关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
person('Jack',24,city='Beijing',job='Engineer')#如果缺少一个命名关键字参数，会报错
#person('Jack',23,'Beijing','Engineer')#命名关键字参数必须传入参数名，这和位置参数不同
#由于调用缺少参数名city和job，Python解释器会把4个参数视为位置参数，但person函数只有两个位置参数，所以会报错
#命名关键字参数可以有缺省值
def person(name,age,*,city='Beijing',job):#命名参数city含有默认值，调用时，可以不传入city参数
	print(name,age,city,job)
person('job',25,job='Engineer')
#注意使用命名关键字参数是，*不是参数，是特殊分隔符，如果缺少，Python解释器将无法识别位置参数和命名关键字参数

#组合关键字参数
#必选参数，默认参数，可变参数，关键字参数，命名关键参数
def f1(a,b,c=0,*args,**kw):#必选，默认，可变，关键字参数
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):#必选，默认，命名关键字，关键字参数
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
f1(1,3)#可变参数元组(),关键字参数是dict{}
f1(1,2,5)
f1(1,2,c=5)
f1(1,2,3,'a')
f1(1,2,3,'a','b',x=99)#可变参数传入的是一个元组，关键字参数必须是关键字-值对应，是一个dict
f2(1,2,d=5,ext=None)
args=(1,2,3,'a')#一个元组tuple
kw={'d':33,'x':'&'}#一个dict
f1(*args,**kw)#args是一个元组，*args是将元组内的元素作为可变参数传入，**kw是将一个dict传入
args=(1,2,3)
kw={'d':99,'x':77}
f2(*args,**kw)
#默认参数一定要用不可变对象
#*args是可变参数，args接收的是一个tuple()
#**kw是关键字参数，kw接收的是一个dict
#命名的关键字参数是为了限制调用可以传入的参数名，也可以提供默认值
#定义命名关键字参数不要忘记写分隔符，否则定义的是位置参数