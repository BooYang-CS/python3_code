#SMTP用于发送邮件
#收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上
#收取邮件最常用的协议是POP协议，现在的版本是3.即POP3
#python内置一个poplib模块，实现了POP3协议，用来直接收取邮件
#POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本。
#要把POP3收取的文本变成可以阅读的邮件，还需要email模块提供的各种类来解析原始文本，变成可阅读的邮件对象

#收取邮件分为两步：
#1.用poplib把邮件的原始文本下载到本地
#2.用email解析原始文本，还原成邮件对象

#用POP3协议下载邮件
import poplib
#输入邮件地址，口令和POP3服务器地址
email=input('Email:')
password=input('Password:')
pop3_server=input('POP3 server:')
#连接到POP3服务器
server=poplib.POP3(pop3_server)
#可以打开或者关闭调试信息
server.set_debuglevel(1)
#可选打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))
#身份认证
server.user(email)
server.pass_(password)
#stat()返回邮件的数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
#list()返回所有邮件的编号:
resp,mails,octets=server.list()
#可以查看返回的列表类似[b'1 2323',b'2 3444']
print(mails)

#获取最新一封邮件，注意索引号从1开始
index=len(mails)
resp,lines,octets=server.retr(index)
#lines存储了邮件的原始文本的每一行
#可以获得整个邮件的原始文本
msg_content=b'\r\n'.join(lines).decode('utf-8')
#稍后解析出邮件
msg=Parser().parsestr(msg_content)

#可以根据邮件索引号直接从服务器删除邮件
#server.dele(index)
#关闭连接
server.quit()

#解析邮件
from email.parsestr import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

#只需要一行代码就可以把邮件内容解析为Message对象
msg=Parser().parsestr(msg_content)
#但是这个Message对象本身是一个MIMEMultipart对象及包含嵌套的其他MIMEBase对象嵌套可能还不止一层
#所以要递归打印出Message对象的层次结构
#indent用于缩进显示
def print_info(msg,indent=0):
	if indent==0:
		for header in ['From','To','Subject']:
			value=msg.get(header,'')
			if value:
				if header='Subject':
					value=decode_str(value)
				else:
					hdr,addr=parsestr(value)
					name=decode_str(hdr)
					value=u'%s<%s>' % (name,addr)
			print('%s%s:%s' % (''*indent,header,value))
	if (msg.is_multipart()):
		parts=msg.get_payload()
		for n,part in enumerate(parts):
			print('%s part %s' % (' '* indent,n))
			print('%s------' % (' ' * indent))
			print_info(part,indent+1)
	else:
		content_type=msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content=msg.get_payload(decode=True)
			charset=guess_charset(msg)
			if charset:
				content=content.decode(charset)
			print('%sText:%s'%(' '* indent,content + '....'))
		else:
			print('%sAttachment:%s' % (' ' * indent,content_type))
#邮件的Subject或者Email中包含的名字都是经过编码后的str,要正常显示，就必须decode
def decode_str(s):
	value,charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value
#decode_header()返回一个list,可能会包含多个邮件地址，所以解析出来的会有多个元素，这里只取第一个元素
#文本邮件的内容也是str,还需要检测编码，否则，非UTF-8编码的邮件都无法显示
def guess_charset(msg):
	charset=msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type','').lower()
		pos=content_type.find('charset=')
		if pos >=0:
			charset=content_type[pos+8:].strip()
	return charset