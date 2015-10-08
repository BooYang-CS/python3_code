#在python中一个.py文件称为一个模块（module）
#为了避免不同的编写的模块名相同的情况，python引入了按目录来组织模块，称为包（package）
'''
每一个包目录下面都会有一个__init__.py的文件，这个文件必须存在的，否则，python就把这个目录
当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有python代码，因为__init__.py本身
就是一个模块，而它的模块名就是顶层包名。
'''
#编写一个hello模块
# -*- coding: utf-8 -*-
'a test module' #表示模块的文档注释，任何模板的第一个字符串都被视为模板的文档注释
__author__='Boo Yang' #作者名
import sys #使用sys模块的第一步，就是导入该模块，导入该模块后就有变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
def test():
	args=sys.argv#sys模块一个argv变量，用list存储了所有命令行的所有参数，argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	if len(args)==1:
		print('hello,world!')
	elif len(args)==2:
		print('hello,%s!' % args[1])
	else:
		print('Too many arguments!')
if __name__=='_main_':
	test()
#运行python3 hello.py获得的sys.argv就是['hello.py','...'](是一个list)
'''
在运行hello模块文件时，python解释器把一个特殊变量__name__置为__main__,
如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块
通过命令运行时执行一些额外的代码，最常见的就是运行测试
'''
