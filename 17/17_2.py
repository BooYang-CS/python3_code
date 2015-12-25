#asyncio是python3.4版本引入的标准库，直接内置了对异步IO的支持
#asyncio的编程模型就是一个消息循环。
#从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程放到EventLoop中执行就实现了异步IO

"""
#例1：用asyncio实现hello world
import asyncio,time
@asyncio.coroutine#把一个生成器generator标记成coroutline类型，然后把这个coroutine放到EventLoop中执行
def prehello():
	print('welcome to world!')
	i=0
	for x in range(100):
		i=i+x
	time.sleep(1)
	return i
def hello():
	print('Hello world!')
	#异步调用asycio.sleep(1)
	#r=yield from prehello()#或者直接调用asycio.sleep(1),yield拿到prehello()函数的返回值，yield from语法方便让我们调用另一个generator。
	r=yield from asyncio.sleep(1)#asyncio.sleep(1)返回None
	print('Hello again! %s' % r)
#获取EventLoop
loop=asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()
'''
yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，
线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。把asyncio.sleep(1)看
成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，
因此可以实现并发执行。
'''
"""
"""
#例2：用Task封装两个coroutine
import threading
import asyncio
@asyncio.coroutine
def hello():
	print('Hello world!(%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % threading.currentThread())
loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
#两个coroutine是由同一个线程并发执行的。
"""
#例3：用asyncio异步网络连接来获取sina,sohu和163的网站首页
import asyncio
@asyncio.coroutine
def webget(host):
	print('webget %s... ' % host)
	connect=asyncio.open_connection(host,80)
	reader,writer=yield from connect
	header='GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line=yield from reader.readline()
		if line==b'\r\n':
			break
		print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
	writer.close()
loop=asyncio.get_event_loop()
tasks=[webget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()