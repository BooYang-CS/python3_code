#多线程
#多任务可以有多进程完成，也可以由一个进程内的多线程完成。
#由于线程是操作系统直接支持的执行单元，python的线程是真正的Posix Thread,而不是模拟出来的线程
'''
python的标准库提供了两个模块:_thread和threading,_thread是低级模块，threading是高级模块,对_thread进行
了封装。绝大多数情况下，只需要使用threading这个高级模块。
'''
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time,threading 
#新线程执行的代码:
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n=0
	while n<5:
		n=n+1
		print('thread %s >>> %s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)#打印当前线程对象的名字
t=threading.Thread(target=loop,name='LoopThread')#创建线程对象，将可调用的对象作为参数传入
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#任何进程默认就会启动一个线程，把线程称为主线程，主线程又可以启动新的线程。
#python的threading模块current_thread()函数，它永远返回当前线程的实例。
#主线程实例的名字为MainThread，子线程的名字在创建时指定。名字在打印时显示，没有其他意义，不起名python也会自动命名。

#Lock
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互补影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据
最大的危险在于多个线程同时修改一个变量。
'''
import time,threading 
balance=0
def change_it(n):
	global balance#定义全局变量，可以使用定义在函数外的变量的值
	balance=balance+n
	balance=balance-n
def run_thread(n):
	for i in range(10000):
		change_it(n)
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#线程的调度室由操作系统决定的，当t1,t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了
#保证一个变量在修改balance的时候，别的线程一定不能修改。
#就要给change_it()上一把锁，当某个线程开始执行change_it()时，加锁后，其他线程就不能调用该函数。
#由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，创建一个锁就是通过threading.Lock()来实现
import time,threading 
balance=0
lock=threading.Lock()
def change_it(n):
	global balance#定义全局变量，可以使用定义在函数外的变量的值
	balance=balance+n
	balance=balance-n
def run_thread(n):
	for i in range(10000):
		lock.acquire()#先获取锁
		try:
			change_it(n)
		finally:
			lock.release()#释放锁
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#当多个线程同时执行lock.acquire()时，只有一个线程能成功获取锁，然后继续执行代码，其他线程继续等待
#获的锁的线程用完后一定要释放锁，否则会成为僵尸进程。所以使用try....finally来确保锁一定会被释放
'''
用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，
但是python不行，因为python解释器执行代码时，有一个GIL锁，Global Interpreter Lock,任何python线程执行前
必须先获得GIL锁，然后，没执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁
实际上把所有线程的执行代码都给上了锁，所以，多线程在python中只能交替执行，即使100个线程跑在100核上，也只能
用到1个核。
python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个python进程有各自独立的GIL锁，互不影响。
'''
#由于python解释器设计有GIL全局锁，导致多钱程无法利用多核，多线程并发在python中难以实现。


