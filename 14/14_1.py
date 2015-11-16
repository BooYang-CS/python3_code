"""
#SMTP发送邮件
#SMTP是发送邮件的协议，python内置对SMTP的支持，可以发送纯文本邮件，HTML邮件以及带附件的邮件
#python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
#构造一个最简单的纯文本邮件
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
import smtplib
def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input("From:")
password=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

msg=MIMEText('hello,send by python! I know who are you!','plain','utf-8')
msg['From']=_format_addr('Python爱好者<%s>' % from_addr)
msg['To']=_format_addr('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候。。。。','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
#编写了一个函数_format_addr()来格式化一个邮件地址。