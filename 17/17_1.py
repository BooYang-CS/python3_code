def consumer():
	r=''
	while True:
		n=yield r;#yield用来定义生成器，可以当成return使用，从函数里返回一个值，yield返回之后可以让函数从上回yield返回的地点继续执行。还可以接收调用者发出的参数
		if not n:
			return 
		print('[CONSUMER] Consuming %s....' % n)
		r='200 OK'#通过yield把结果传回
def produce(c):
	c.send(None)#调用c.send(None)启动生成器，生成器是在循环的过程中不断推算后续的元素。
	n=0
	while n<5:
		n=n+1
		print('[PRODUCER] Producing %s...' % n)#生产产品
		r=c.send(n)#切换到consumer执行，并给生成器传递参数，yield产生生成器并接受参数
		print('[PRODUCER] Consumer return : %s' % r)
	c.close()

c=consumer()
produce(c)
'''
总的来说，协程就是生成器来产生的，用yield来产生生成器，并且可以用来接收调用者发出的参数，
并且可以将结果返回
'''