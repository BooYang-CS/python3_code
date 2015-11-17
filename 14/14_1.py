"""
#SMTP发送邮件
#SMTP是发送邮件的协议，python内置对SMTP的支持，可以发送纯文本邮件，HTML邮件以及带附件的邮件
#python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

#1. 构造一个最简单的纯文本邮件

from email.mime.text import MIMEText
msg=MIMEText('hello,send by python ....','plain','utf-8')
#构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype,传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
#然后通过SMTP发出去
from_addr=input('From:')#出入email地址和口令
password=input('Password:')
to_addr=input('To:')#输入收件人地址
smtp_server=input('SMTP server:')#输入SMTP服务器地址
import smtplib
server=smtplib.SMTP(smtp_server,25)#SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
#利用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
'''
SMTP协议就是简单的文本命令和响应，login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以
一次发给多个人，所以传入一个list,有邮件正文是一个str,as_string()把MIMEText对象变成str.
'''
#注意使用qq邮箱发送邮件时，登录的账号要开启SMTP服务，qq默认是关闭STMP服务的。
"""
#给邮件添加主题，发件人，收件人信息，一封完整的邮件
from email import encoders
from email.header import Header 
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
def _format_addr(s):
	name,addr=parseaddr(s)#用来解析字符串中email地址
	print(name)
	print(addr)
	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input("From:")
password=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

"""
#2. 发送html邮件和纯文本邮件

#msg=MIMEText('hello,send by python! I know who are you!','plain','utf-8')
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)#注意收件人的邮件地址的格式必须用<>
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候。。。。','utf-8').encode()
"""
msg=MIMEMultipart()#这个代表邮件本身是一个整体
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候。。。。','utf-8').encode()
#邮件正文是MIMEText，并将其添加到MIMEMultipart中
#msg.attach(MIMEText('i will send a file to you ,please check it','plain','utf-8'))#只发送纯文本
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))#发送HTML邮件并嵌入附件图片
#添加附件就是加上一个MIMEBase,从本地选一个文件
with open('text.png','rb') as f:
	#设置附件的MIME和文件名，这里是png类型
	mime=MIMEBase('image','png',filename='text.png')
	#加上必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='text.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-ID','0')
	#把附件的内容读进来
	mime.set_payload(f.read())
	#用Base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMultipart
	msg.attach(mime)
#开始发送邮件
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)#打印出和服务器交互的所有信息
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
#编写了一个函数_format_addr()来格式化一个邮件地址。 
#经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本。

#3. 发送HTML邮件
#发送的邮件如果不是纯文本，在构造MIMEText对象时，把HTML字符传进去，再把第二个参数有plain编程html就可以了
'''
msg=MIMEText('<html><body><h1>Hello</h1>'+'<p>send by<a href="http://www.python.org">python</a>...</p>'+'</body></html>','html','utf-8')
'''
#4. 发送附件

#如果要发送附件，带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身。
#可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，在继续往里面加上表示附件的MIMEBase对象即可
#邮件对象MIMEMultipart
'''
msg=MIMEMultipart()#这个代表邮件本身是一个整体
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候。。。。','utf-8').encode()
#邮件正文是MIMEText
msg.attach(MIMEText('i will send a file to you ,please check it','plain','utf-8'))
#添加附件就是加上一个MIMEBase,从本地选一个文件
with open('text.png','rb') as f:
	#设置附件的MIME和文件名，这里是png类型
	mime=MIMEBase('image','png',filename='text.png')
	#加上必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='text.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-ID','0')
	#把附件的内容读进来
	mime.set_payload(f.read())
	#用Base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMultipart
	msg.attach(mime)
'''
#5. 直接发送图片
'''
把图片嵌入到邮件正文中，直接在HTML邮件中链接图片地址会被屏蔽，要把图片嵌入到邮件中，只需要按照发送附件的方式，
先把邮件作为附件添加进去,然后再HTML中通过引用src="cid:0"就可以把附件作为图片嵌入，如果与多个图片，给他们依次编号，
然后引用不同的cid:x即可。
'''
"""
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))
"""
#6. 同时发送HTML和plain格式
#利用MIMEMultipart就可以组合一个HTML和plain,要注意subtype是alternative,如果用户设备无法查看HTML邮件，会直接降级为纯文本邮件
"""
msg=MIMEMultipart('alternative')
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候。。。。','utf-8').encode()

msg.attach(MIMEText('hello','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
"""

#7.加密SMTP
#使用标准25端口连接SMTP服务器时，使用明文传送，不太安全。可以加密SMTP会话，实际上就是先创建SSL安全连接，在使用SMTP发送邮件
#例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
#Gmail的SMTP端口是587
"""
smtp_server='smtp.gmail.com'
smtp_port=587
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
#剩下的代码前面一样
"""

#8.总结
"""
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，
就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
"""