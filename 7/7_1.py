#错误处理
'''
在程序运行的过程中，如果发生错误，可以返回一个错误代码。
'''
#1.try
try:
	print('try.....')
	r=10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')
'''
当认为某些代码可能会出错，就可以用try来运行这段代码，如果执行错误，则后续代码不会继续执行，而是直接跳转
至错误处理代码即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''

#没有错误发生，except语句块就不会执行，但是finally如果有，则一定会被执行(可以没有finally语句)
#如果发生不同类型的错误，应该不同的except语句块处理。
try:
	print('try.....')
	r=10/int('23.33')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
finally:
	print('finally....')
print('END')
#int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError.
#如果没有错误发生，可以在except语句块后面加上一个else，当没有错误发生时，会自动执行else语句。
try:
	print('try......')
	r=10/int('2')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')


'''
python的错误其实也是class，所有的错误类型都继承BaseException，所以在使用except时需要注意的是，它不但捕获该
类型的错误，还把其子类错误也包括进去了。
try:
	foo()
except ValueError as e:
	print('ValueError')
except UnicodeError as e:
	print('UnicodeError')
'''
#第二个except永远也不会捕获到UnicodeError，因为UnicodeError是ValueError的子类，如果有也是第一个except给捕获了


'''
使用try...except捕获错误就可以跨越多层调用，比如函数main()调用foo(),foo()调用bar(),结果bar()出错了，这是，只要
main()捕获到了，就可以处理
'''
def foo1(s):
	return 10/int(s)
def bar1(s):
	return foo1(s)*2
def main():
	try:
		bar1('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally....')
m=main()
m
#不需要再每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。


#调用堆栈,如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
'''
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	bar('0')
main()
#会出现错误，解释器会逐步打印错误堆栈，最后确定错误信息
Traceback (most recent call last):
  File "7_1.py", line 84, in <module>
    main()
  File "7_1.py", line 83, in main
    bar('0')
  File "7_1.py", line 81, in bar
    return foo(s)*2
  File "7_1.py", line 79, in foo
    return 10/int(s)
ZeroDivisionError: division by zero
如果不捕获错误，自然可以让python解释器打印出错误堆栈，但是程序也结束了。既然可以捕获错误，就可以把错误
堆栈打印出来，然后分析错误原因，同时让程序继续执行下去。
'''
#python内置的logging模块可以非常容易地记录错误信息
import logging
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('END')
#同样的错误，但是程序打印完错误信息后会继续执行，并正常退出
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查

'''
因为错误是class，抓获一个错误就是捕获到该class的一个实例，因此，错误不是凭空产生的，而是有意创建并抛出的。
python的内置函数会抛出多类型的错误，自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，定义一个错误的class，选好继承关系，然后，用raise语句抛出一个错误的实例
'''
"""
class FooError(ValueError):#错误class继承至ValueError
	pass
def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value:%s' %s)
	return 10/n
foo('0')
"""
#只有在必要的时候才定义自己的错误类型。

"""
def foo3(s):
	n=int(s)
	if n==0:
		raise ValueError('invalid value:%s'% s)
	return 10/n
def bar3():
	try:
		foo3('0')
	except ValueError as e:
		print('ValueError!')
		raise
bar3()
"""
#在bar()函数中，先打印一个ValueError后，又把错误通过raise语句抛出去。
#这种处理方式比较常见，先捕获错误记录一下，在讲错误往上抛，让顶层调用者去处理。
#raise语句如果不带参数，就会把错误原样抛出。
#在except中raise一个Error，可以把一种类型的错误转化为另一种类型
try:
	10/0
except ZeroDivisionError:
	raise ValueError('input error')
'''
#错误信息：
Traceback (most recent call last):
  File "7_1.py", line 150, in <module>
    10/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "7_1.py", line 152, in <module>
    raise ValueError('input error')
ValueError: input error
'''