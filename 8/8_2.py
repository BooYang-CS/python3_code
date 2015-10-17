#StringIO 和 BytesIO()
#很多时候，数据读写不一定是文件，也可以在内存中读写
#StringIO顾名思义就是在内存中读写str
#要把str写入StringIO,需要先创建一个StringIO,然后像文件一样写入即可：
from io import StringIO
f=StringIO()#创建一个StringIo
print(f.write('hello'))#f.write()返回的是字符串的长度
print(f.write(','))
print(f.write('world!'))
print(f.getvalue())
#getvalue()方法用于获得写入后的str
#要读取StringIO，可以用一个str初始化StringIO,然后像文件一样读取：
from io import StringIO
f=StringIO('hello!\nHi!\nGoodbye!')
while True:
	s=f.readline()#注意读取文件的readlines()和StringIO的readline()
	if s=='':
		break
	print(s.strip())
#readline()每次读取一行，当前位置一道下一行
#readlines()读取整个文件的所有行，保存在一个列表list变量中，每行作为一个元素
#read(size)从文件当前位置起读取size字节。如果size是负值或者省略，读取文件到结束，返回结果是一个字符串。

#BytesIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
#BytesIO实现了在内存中读取bytes，我们创建一个BytesIO,然后写入一些bytes
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#写入的不是str，而是进过UTF-8编码的bytes
#和StringIO类似，可以用一个bytes初始化的BytesIO，然后，像读文件一样读取
from io import StringIO
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
#StringIo和BytesIo是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。