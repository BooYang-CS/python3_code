#多进程
#1. windows平台单进程创建
#python的os模块封装了常见的系统调用，其中个就包括fork,可以在python程序中轻松创建子进程
'''
import os
print('Process (%s) start...' % os.getpid())
#only works on unix/mac/linux
pid=os.fork()
if pid==0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(),pid))
'''
#由于windows没有fork调用，上面的代码在windows上无法运行。
#由于python是跨平台的，自然也应该是提供一个跨平台的多进程支持。
#multiprocessing模块就是跨平台版本的多进程模块
#multiprocessing模块提供一个process类来代表一个进程对象。
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__=='__main__':#表示下面这个程序只能在这个模块中执行，如果在其他模块中导入这个模块，下面的程序会不执行
	print('Parent process %s.' % os.getpid())
	p=Process(target=run_proc,args=('test',))#执行函数run_proc()并且该函数的传入参数为args
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')
'''
__name__=='__main__'就是让你写的脚本模块既可以导入到别的模块中用，另外该模块也可以自己执行。
直接执行某个.py文件的时候，该文件中那么"__name__=='__main__'" 是True，但是如果我们从另外一个.py文件
通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main_。
'''
#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

#2.进程池，多进程创建
'''
如果要启动大量的子进程，可以用进程池的方式批量创建子进程,进程池的实例对象的apply_async()属性传入函数和传入参数
'''
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start=time.time()#记录任务执行的开始时间
	time.sleep(random.random()*2)
	end=time.time()#记录任务结束的结束时间
	print('Task %s runs %0.2f seconds.' % (name,(end-start)))#打印任务的执行时间
if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p=Pool(5)
	for i in range(5):#i从0开始调用直到4
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocess done...')
	p.close()
	p.join()
	print('All subprocess done.')
'''
对Pool对象调用join()方法(可以理解为系统为回收资源做准备)会等待所有子进程执行完毕，调用join()之前必须先调用close()
，调用close()之后就不能继续添加新的Process了。
Task 0，1，2，3，4是立即执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小可能是4，因此默认
最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成p=Pool(5),就可以同时跑5个进程
#Pool的默认大小一般是cpu的内核数。
'''
#3. 子进程
#子进程并不是自身，而是一个外部进程。创建子进程后，还需要控制子进程的输入和输出
#subprocess模块可以让我们非常方便的启动一个子进程，然后控制其输入和输出
'''
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])#子进程调用方法（这里的方法是windows系统命令）和传入参数
print('Exit code:',r)
'''
#程序的运行结果和nslookup www.python.org一样的
#如果子进程还需要输入，则可以通过communicate()方法输入:
'''
import subprocess
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))#在windows下改为gbk输出
print('Exit code:',p.returncode)
'''
#上面的代码相当于在命令行执行命令nslookup,然后手动输入:set q=mx python.org exit 
#subprocess这个模块来产生子进程，并连接到子进程的标准输入/输出/错误中去,还可以得到子进程的返回值。
#subprocess模块定义了一个类Popen,这个类已有很多参数。
'''
class subprocess.Popen( args, bufsize=0,stdin=None,stdout=None, stderr=None, creationflags=0)
args参数。可以是一个字符串，可以是一个包含程序参数的列表。
stdin    表示子进程的标准输入
stdout   表示子进程的标准输出
stderr   表示子进程的标准错误
这三个参数的可选的值有PIPE或者一个有效的文件描述符（其实是个正整数）或者一个文件对象，还有None。
如果是PIPE，则表示需要创建一个新的管道，如果是None，不会做任何重定向工作，子进程的文件描述符会继承父进程的。
另外，stderr的值还可以是STDOUT，表示子进程的标准错误也输出到标准输出。

subprocess.call()函数 ，执行命令，并等待命令结束，在返回子进程的返回值。

Popen对象属性值
communicate()参数是标准输入，返回标准输出output和标准错误err
returncode 进程返回值 
'''
#4. 进程间的通信
#Process之间肯定要通信的python的multiprocessing模块包装了底层的机制，提供了Queue，Pipes等方式来交换数据
'''
#do_queue.py
from multiprocessing import Process,Queue
import os,time,random
#写进程执行的代码:
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...',% value)
		q.put(value)
		time.sleep(random.random())
#读数据进程执行的代码:
def read(q):
	print('Process to read: %s',% os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.' % value)
if __name__='__main__':
	#父进程创建Queue，并传给各个子进程
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	#启动子进程pw,写入
	pw.start()
	#启动子进程pr，读取
	pr.start()
	#等待pw结束
	pw.join()
	#pr进程是死循环，无法等待期结束，只能强行终止
	pr.terminate()
'''
#在unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
#由于windows没有fork调用，因此，multiprocessing需要'模拟'出fork的效果，父进程所有python对象都必须pickle序列化再传到子进程。
#所以multiprocessing在windows下调用失败了，要先考虑是不是pickle失败了

