#操作文件和目录
import os
print(os.name)#操作系统的类型
#python内置的os模块也可以直接调用操作系统提供的接口函数
#print(os.uname)#获取详细的系统信息，uname()函数在windows系统上不提供，os模块的某些函数是跟操作系统相关的

#环境变量
#操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
#要获取某个环境变量的值，可以用os.environ.get('key')
print(os.environ.get('PATH'))
print(os.environ.get('x','default'))

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中。
print(os.path.abspath('.'))#查看当前目录的绝对路径
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('./','testdir')#列出新目录的完整路径,./表示当前目录
os.mkdir('./testdir')#然后创建一个目录
os.rmdir('./testdir')#删除一个目录
'''
把两个路径合成一个时，不要直接拼接字符串，而是通过os.path.join()函数,这样可以正确处理不同
操作系统的路径分隔符。
在linux/unix/mac下，os.path.join()返回这样的字符串:path1/path2
在windows下，会返回这样的分隔符:path1\part2
同样的道理，要拆分路径时，也不要直接去拆字符串，而是通过os.path.split()函数。这样可以把一个
路径拆成两部分，后一部分总是最后级别的目录或文件名。
'''
print(os.path.split('/Users/yangbo/testdir/file.txt'))
#('/Users/yangbo/testdir','file.txt')
print(os.path.join('/Users/yangbo/testdir','file.txt'))
#/Users/yangbo/testdir\file.txt
#这些合并和拆分路径的函数并不要求目录和文件真是存在，它们只对字符串操作。
#文件操作使用下面的函数:
os.rename('test.txt','test11.txt')
os.rename('test11.txt','test.txt')#对文件进行重命名
#删除文件
#os.remove('test.py')
#复制文件在os模块中并不存在，因为复制文件并非由操作系统提供的系统调用。可以由读写文件完成文件复制
#但是shutil模块提供了copyfile()的函数，还可以在shutil模块中找到很多实用的函数，可以看做是对os模块的补充

print([x for x in os.listdir('./') if os.path.isdir(x)])#./表示当前目录,列出所有当前目录下的所有目录
#listdir是目录列表，isdir()判断一个是不是目录文件
print([x for x in os.listdir('./') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
#列出所有.py文件。isfile()判断是否是文件。splitext是用来分解文件的扩展名。
'''
练习1：利用os模块编写一个能实现dir -l输出的程序。
'''
from datetime import datetime
import os
pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')
for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
'''
练习2:编写一个程序，能在当前目录以及目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
'''
import os
def ListFile(dir):#获取当前目录的文件
	return [x for x in os.listdir(dir) if os.path.isfile(x)]
def ListDir(dir):#获取当前目录的子目录
	return [x for x in os.listdir(dir) if os.path.isdir(x)]
def ListDirPath(dir):#获取当前目录的子目录的相对路径
	buffer=ListDir(dir)
	return [os.path.join(dir,x) for x in buffer]
def IsSubdir(dir):#判断当前目录是否有子目录
	if ListDir(dir)==[]:
		return False
	else:
		return True
def GetFileName(file):#将扩展名去掉获取文件名
	return os.path.splitext(file)[0]
def SearchStringDir(dir,str):#搜索当前目录中文件名是否含有对应字符串的文件
	buffer=[]
	for x in ListFile(dir):
		if GetFileName(x).find(str)!=-1:
			buffer.append(x)
	buffer=[os.path.join(dir,j) for j in buffer]#重组符合条件的文件的路径
	return buffer
def NextFolds(folds):#获取一串目录的所有子目录，若无子目录则返回空列表
	buffer=[]
	for x in folds: #相对路径
		if IsSubdir(x)==False:
			pass
		else:
			buffer=buffer+ListDirPath(x)
	return buffer
def SearchStringSubdir(dir,str):#搜索当前目录及所有子目录中文件名含有对应字符串的文件
	buffer=[]
	folds=[dir]
	while True:
		if NextFolds(folds)==[]:#若一串目录无子目录，则在其中进行搜索后即停止搜索
			for x in folds:
				buffer=buffer+SearchStringDir(x,str)
			break
		else:
			for x in folds:#若以串目录有子目录，在这些子目录中继续搜索
				buffer=buffer+SearchStringDir(x,str)
			folds=NextFolds(folds)
	return buffer
print(ListFile('./'))#打印当前目录的所有文件
print(ListDir('./'))#打印当前目录的所有子目录
print(ListDirPath('./'))#打印当前目录的所有子目录的相对路径
print(IsSubdir('./'))#判断当前目录是否有子目录
print(GetFileName('test.txt'))#获得文件扩展名
print(SearchStringDir('./','test'))#搜索当前目录中文件名是否含有对应字符串的文件
print(NextFolds('./'))
print(SearchStringSubdir('./','test'))#搜索当前目录及所有子目录中文件名含有对应字符串的文件