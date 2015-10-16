#IO编程
'''
在IO编程中，Stream(流)是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但只能单向流动。
Input Stream就是数据从外面(磁盘，网络)流进内存，Output Stream就是数据从内存流到外面去。
#cpu和读写速度不匹配问题
1.同步IO，CPU等待数据读写完毕再执行程序
2.异步IO,CPU不等待IO结果，执行后续代码，但是比较复杂
'''
#读写文件
#1.读文件 
#要以读文件的模式打开一个文件对象，使用python内置的open()函数，传入文件名和标示符
f=open('./test.txt','r')#标识符'r'表示读。
#如果文件不存在，open()函数会抛出一个IOError错误，并且给出错误码和详细的信息。
#如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容。python被内容读到内存，用一个str对象表示
print(f.read())
print(f)
#最后一步就是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()#打印print(f.close())试试，返回None
#文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用，所以，为了保证无论出错都能正确关闭文件，可以使用try...finally来实现
try:
	f=open('./test.txt','r')
	print(f.read())
finally:
	if f:
		f.close()
#但是每次这么写比较繁琐，所以python引入了with语句来自动帮我们调用close()方法
with open('./test.txt','r') as f:
	print(f.read())
#实现功能和try...finally一样，但是代码简洁

'''
调用read()会一次性读取文件的全部内容，如果文件很大，内存可能就装不下了。为了保险起见，可以反复调用
read(size)方法，每次最多读取size个字节的内容。
调用readlines()一次性读取所有内容并按行返回。因此根据需要决定怎么调用。
如果确定文件小，使用read()很方便。
如果不确定文件大小，反复调用read(size)比较保险。
如果是配置文件，调用readlines()最方便。
'''
f=open('./test.txt','r')
'''
for line in f.readlines():
	print(line.strip())#把末尾的'\n'删掉,时期打印结果和源文件一样
'''
print(f.readlines())#结果是这样的新式:['123123123123\n', '123123123\n', '123123']

#file-like Object 
#像open()函数返回的这种有个read()方法的对象，在python中统称为file-like-Object。还有内存的字节流，网络流等等
#file-like Object不要求从特定的类继承，只要写个read()方法就行
#StringIO就是在内存中创建的file-like Object,常用作临时缓冲

#二进制文件
#前面讲的都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片，视屏等等。用'rb'模式打开即可
f=open('./test.jpg','rb')
f.read()#print(f.read())#结果是使用十六进制表示的一个个字节
f.close

#字符编码’
#要读取非UTP-8编码的文本文件，需要给open()函数传入encoding参数。例如，读取GBK编码的文件,比如中文
f=open('./test1.txt','r',encoding='gbk')#如果用这个模式读取UTF-8文件，则什么都读不到
print(f.read())
f.close()
#遇到有些编码不符合规范的文件，可能会遇到UnicodeDecodeError。因为文本文件中可能参杂了一些非法编码的字符。
#遇到这种情况，open()函数还要接受一个errors参数，表示遇到错误编码后如何处理。最简单的方法是直接忽略
f=open('./test2.txt','r',encoding='gbk',errors='ignore')
print(f.read())
f.close()

#写文件
#写文件和读文件一样，唯一的区别是调用open()函数时，传入标识符'w'或者'wb'来表示文本文件或二进制文件
f=open('./test.txt','w')
f.write('hello,world')
f.close
#向一个文件写内容，会把原来的内容擦除掉。
#可以反复调用write()来写文件，但是务必调用f.close()来关闭文件。
#当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是方法内存缓存起来，空闲的时候在慢慢写入。
#只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
#忘记调用close()的后果就是数据可能只写了一部分的磁盘，剩下的就丢失了。推荐使用with语句
with open('./test.txt','w') as f:
	f.write('welcome to world,')
	f.write('hello,world!')
#这两个write是按行连续写入，不是单独调用。
#要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
with open('./test3.txt','w',encoding='gbk') as f:
	f.write('你好，世界')

