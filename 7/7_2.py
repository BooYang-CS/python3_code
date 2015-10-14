#程序调试，遇到程序出错，就需要调试bug
#1.最直接的方法是用print()把所有可能有问题的变量打印出来
def foo(s):
	n=int(s)
	print('>>>n=%d' % n)
	return 10/n
def main():
	foo('2')
main()
#用print()来辅助查看，将来还得删除它，运行结果也会包含很多垃圾信息
#凡是用print()来辅助查看的地方，都可以用断言(assert)来替代
def foo(s):
	n=int(s)
	assert n!=0,'n is zero!'
	return 10/n
def main():
	foo('3')
#assert的意思，表达式n!=0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
#如果断言失败，assert语句本身就会抛出AssertionError
main()
#如果到处充斥着assert，也比较烦。不过，启动python解释器时可以用-O(大写的O)参数来关闭assert
#python -O 7_2.py

#3.logging
#把print()替换为logging是第三种方式，和assert比，logging不会抛出错误，而且可以输出文件
"""
import logging
s='5'
n=int(s)
logging.info('n=%d' % n)
print(10/n)
#logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError,没有任何信息
"""
#在import logging之后添加一行配置
import logging
logging.basicConfig(level=logging.INFO)
s='4'
n=int(s)
logging.info('n=%d' % n)
print(10/n)
'''
logging可以指定记录信息的级别，有debug,info,warning,error等几个级别。当我们指定level=INFO时，
logging.debug就不起作用了。当指定level=WARNING后，debug和info就不起作用了。这样就可以输出不同级别的
信息，也不用删除，最后同意输出那个级别的信息.
'''
#logging的另一个好处就是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

#4.pdb
#第四种方法就是启动python的调试器pdb，让程序一单步方式运行，可以随时查看运行状态。
s='7'
n=int(s)
print(10/n)
#以参数-m pdb启动后，pdb定位到下一步执行的代码。输入命令1来查看代码
#输入命令n可以单步执行代码
#任何时候都可以输入命令 p 变量名 来查看变量
#输入命令q结束调试，退出程序
#如果代码行数过多，就比较麻烦，这时就需要另一种方法pdb.set_trace()了
#使用pdb.set_trace()不需要单步调试，只需要import pdb，然后再可能出错的地方放一个pdb.set_trace(),可以设置一个断点
import pdb
s1='0'
n=int(s1)
pdb.set_trace()#程序运行到这里会自动暂停
print(10/n)
#程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行

#5.IDE，要像vs一样调试程序，就只有使用IDE了，比较好的python IDE有Pycharm