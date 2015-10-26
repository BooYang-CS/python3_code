#1. struct
#struct的pack函数把任意数据类型编程bytes
import struct
print(struct.pack('>I',10240099))
#pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian(大端)，也就是网络序，I表示4字节无符号整数。
#后面的参数个数要和处理指令一致。
#unpack把bytes变成相应的数据类型
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
#所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

#2. 摘要算法如MD5,SHA1
#摘要算法有称哈希算法，散列算法，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串。
#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
#摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
import hashlib
md5=hashlib.md5()
md5.update('hello world,welcome to new world!'.encode('utf-8'))
print(md5.hexdigest())
#如果数据量很大，可以分块多次调用update(),最后计算的结果是一样的
import hashlib
md5=hashlib.md5()
md5.update('hello world'.encode('utf-8'))
md5.update(',welcome to new world!'.encode('utf-8'))
print(md5.hexdigest())
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit（16字节），通常用一个32位的16进制字符串表示。
#另一种常见的摘要算法是SHA1,调用SHA1和调用MD5完全类似
import hashlib
sha1=hashlib.sha1()
sha1.update('hello world,welcome to new world1'.encode('utf-8'))
print(sha1.hexdigest())
#ShA1的结果是160bit（20字节）,通常是一个40位的16进制字符串表示

#3.摘要算法的应用
#1.网站用户的口令保存方式，不是存储用户的明文口令，而是存储用户口令的摘要，比如MD5
#当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。
#存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
'''
def calc_md5(password):
    return get_md5(password + 'the-Salt')
'''
#如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
'''
练习:设计一个用户登录验证,使用用户名作为MD5存储
'''
#存储数据中用户的登录密码的md5值
db={}
def get_md5(str):#通过字符串得到MD5值
	md5=hashlib.md5()
	md5.update(str.encode('utf-8'))
	return md5.hexdigest()
def register(user,pw):#输入用户名和密码，得到密码的MD5值
	db[user]=get_md5(pw+user+'the-Salt')#存储用户的md5值 
def login(user,pw):#用户登入
	if(user in db):
		if get_md5(pw+user+'the-Salt')==db[user]:
			print('login sucessfully!')
		else:
			print('password incorrect!')
	else:
		print('user does not exist!')
if __name__=='__main__':
	while True:
		n=input('choose your action,1 or 2 1:login 2:register\n')
		if n=='1':
			username=input('enter your username:')
			password=input('enter your password:')
			login(username,password)
		elif n=='2':
			username=input('enter your username:')
			password=input('enter your password:')
			register(username,password)
		else:
			pass
