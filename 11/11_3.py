#Base64
#Base64是一种用64个字符来表示任意二进制数据的方法
'''
Base64的原理很简单，首先，准备一个包含64个字符的数组,然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit,
划为4组，每组正好6个bit,这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
'''
import base64
print(base64.b64encode(b'binary\x00string'))#编码
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))#解码
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_.
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
#Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
'''
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
因此，如果去掉=后的Base64编码长度不是4的整数倍，那么就需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
'''
print(base64.b64encode(b'abcd'))#编码
print(base64.b64decode(b'YWJjZA=='))#解码
#如果要编码的二进制数据不是3的倍数，Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
'''
练习：写一个能处理去掉=的base64解码函数
'''
import base64
def safe_base64_decode(s):
	a=(-len(s))%4#字节长度是否是4的整数倍，如果是则是没有去=的base64编码
	if isinstance(s,str):
		s=s+'='*a
		return base64.b64decode(s.encode('utf-8'))
	else:
		s=s+b'='*a
		return base64.b64decode(s)
print(safe_base64_decode(b'YWJjZA'))#对b'abcd'编码并去掉=后的base64编码进行解码，可以正确得到b'abcd'
print(safe_base64_decode(b'YWJjZA=='))