'''
偏函数
'''
print(int('12345'))#int()函数默认按十进制转换成整数
print(int('12345',base=8))#int函数有base参数，默认值是10，如果传入base参数就可以将字符串按N进制转换成十进制整数
#如果要转换大量的二进制字符串，每次传入int(x,base=2)非常麻烦，这里可以定义int2函数
def int2(x,base=2):
	return int(x,base)
print(int2('1000000'))
#functools.partial就是创建一个偏函数，不需要自己定义int2(),可以直接使用下面代码创建一个新的函数int2
import functools
int2=functools.partial(int ,base=2)
print(int2('100100101'))
'''
functools.partial的作用就是将一个函数的某些参数固定住（也就是设置默认值），返回一个新的函数，调用这个
函数会很简单。上面新的int2函数，仅仅是把base参数重新设定默认值2，但也可以在函数调用时传入其他值。
'''
print(int2('100000',base=10))
print(int2('100000'))
'''
创建偏函数时，实际上可以接受函数对象，*args(可变参数)和**kw（关键字参数）这3个参数。
当传入int2=functools.partial(int,base=2)
int2('10010')相当于：
kw={'base':2}
int('10010',**kw)
另外，例如:
max2=functools.partial(max,10)#实际上会把10作为*args(可变参数)的一部分自动加到左边
max2(5,6,7)
#相当于：
args=(10,5,6,7)
max(*args)
#当函数的参数个数太多时，使用functools.partial可以创建一个新的函数，这个新的函数可以固定原函数的部分
参数，从而在调用时更简单。
'''

