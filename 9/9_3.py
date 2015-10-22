#1. ThreadLocal
import threading 
#创建全局ThreadLocal对象:
local_school=threading.local()
def process_student():
	#获取当前线程关联的student:
	std=local_school.student
	print('Hello,%s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student=name
	process_student()
t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
#threading.Thread()创建线程对象，target传入线程函数，args传入的函数的参数，name给创建的线程自定义命名
t1.start()
t2.start()
t1.join()
t2.join()
'''
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
可以把local_school看成局部变量，但每个属性如了local_student.student都是线程的局部变量，可以任意读写
而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
'''
#可以理解全局变量local_school是一个dict,不但可以用local_school.student,还以绑定其他变量local_school.teacher。
#ThreadLocal最常用的地方就是为每一个线程绑定一个数据库连接，HTTP请求，用户身份信息等，线程调用的处理函数可以方便访问资源

#2.分布式进程
'''
在Thread(线程)和Process(进程)中，优先选Process，因为Process更稳定。而且Process可以分布到多台机器上，
而Thread最多只能分布到同一台机器的多个CPU上。
#Python 的multiprocessing 模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上，一个
服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解
网络通信的细节，就可以很容易编写分布式多进程程序。
'''
#一个通过Queue通信的多进程程序在同一台机器上运行，希望把发送任务的进程和处理任务的进程分布到两台机器上
#通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
#服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务
"""task_master.py"""
import random,time,queue 
from multiprocessing.managers import BaseManager
#发送任务的队列
task_queue=queue.Queue()
#接受结果的队列
result_queue=queue.Queue()
#从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
	pass
#把两个Queue都注册到网上，callable参数关联了Queue对象:
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
#绑定端口5000，设置验证码'abc'
manager=QueueManager(address=('',5000),authkey=b'abc')
#启动Queue
manager.start()
#获得通过网络访问的queue对象：
task=manager.get_task_queue()
result=manager.get_result_queue()
#放几个任务进去
for i in range(10):
	n=random.randint(0,10000)
	print('Put task %d...',%n)
	task.put(n)
#从result对读取结果
print('Try get results...')
for i in range(10):
	r=result.get(timeout=10)
	print('Result: %s' % r )
#关闭
manager.shutdown()
print('master exit.')
'''
在一台机器上写多进程时，创建的Queue可以直接拿来用，但是在分布式进程环境下，添加任务到Queue不可以直接
对原始的task_queue进行操作，那样绕过了Queuemanager的封装，必须通过manager.get_task_queue()获得Queue的接口添加
'''
"""task_worker.py"""
import time,sys,queue
from multiprocessing.managers import BaseManager
#创建类似的QueueManager:
class QueueManager(BaseManager):
	pass
#由于这个QueueManger只能从网络上获取Queue，所以注册时只提供名字；
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器，也就是运行task_master.py的机器
server_addr='127.0.0.1'
print('Connect to server %s...',% server_addr)
#端口和验证码注意保持和task_master.py设置的完全一致：
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接:
m.connect()
#获取Queue的对象
task=m.get_task_queue()
result=m.get_result_queue()
#从task队列取任务，并把结果写入result队列
for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d * %d...',% (n,n))
		r='%d * %d = %d ' % (n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is Empty')
#处理结束
print('worker exit..')
'''
1. task_master.py 和task_worker.py是一个简单的分布式计算，把代码稍加修改启动多个worker，就可以把任务
分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
2. 注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中。
3. Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，
所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
'''