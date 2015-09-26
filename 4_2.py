'''
filter()函数用于过滤序列，filter()也接收一个函数和一个序列，filter()把传入的函数依次作用于每个元素
然后根据返回值是True还是False决定保留还是丢弃该元素,最后的结果返回一个Iterator,这一点与map类似
'''
def is_odd(n):
	return n%2==1
print((filter(is_odd,[1,2,3,4,5,6,7,8,9])))#只保留列表中的奇数，删掉偶数
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
#filter()函数返回的是一个Iterator,是一个惰性序列，要使filter()完成计算结果，需要list()函数获得结果并返回list
'''
用filter()求素数:
埃氏筛选法：
列出从2开始的所有自然数，构造一个序列，取序列第一个数，它一定是素数，然后用2把序列的2的
倍数筛选掉，取新序列的第一个数3，它一定是素数，然后用3把序列3的倍数筛选掉。不断筛选下去
就可以得到所有素数
'''
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n#构造一个从3开始的奇数序列，生成器就是可以按照某种算法推算列表元素，不必创建完整的list
def _not_divisible(n):
	return lambda x:x%n>0
def primes():
	yield 2#第一个素数是2，加入素数的生成器中
	it=_odd_iter()#it是以3开始的奇数序列生成器
	while True:
		n=next(it)#n=3
		yield n#将3加入素数序列生成器中
		it=filter(_not_divisible(n),it)#重新生成奇数序列生成器it，过滤是3的整数倍的数即x%n>0，其中x=3,5,7,9...,n=3
for n in primes():
	if n<100:
		print(n)
	else:
		break
'''
练习：回数是指从左读和从右读都是一样的数，请用filter过滤掉非回数。
'''
#方法1
def is_palindrome(n):
	s=str(n)#先将整数转换成字符串
	for n in range(len(s)):#range(x)是产生从0开始到x-1的自然数
		if s[n]!=s[len(s)-1-n]:
			return False
	return True
output=filter(is_palindrome,range(1,1000))#filter返回的是一个Iterator，需要用list返回完整的结果
print(list(output))
#方法2
def is_palindrome(n):
	return str(n)==str(n)[::-1]#将字符串反转过来，判断两个字符串是否一样，返回布尔值
output=filter(is_palindrome,range(1,1000))
print(list(output))

