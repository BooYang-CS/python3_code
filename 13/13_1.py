#TCP编程，打开一个Socket需要知道目标计算机的ip地址和端口号，再指定协议类型即可
#创建一个基于TCP链接的Socket
import socket #导入socket库
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.qq.com',80))#连接ip和web固定端口号，参数是一个tuple
#创建scoket,AF_INET指定使用IPV4协议，AF_INET6为IPv6协议。SOCK_STREAM指定使用面向使用字节流的TCP协议
#建立TCP连接后，向服务器发送请求，要求返回首页内容
s.send(b'GET / HTTP/1.1\r\nHost: www.qq.com\r\nConnection: close\r\n\r\n')

#HTTP协议规定客户端必须先发送请求给服务器，服务器收到后才发送数据给客户端
#接收数据
buffer=[]
while True:
	#每次最多接收1k数据
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=b''.join(buffer)

#数据接收完后，调用close()方法关闭Socket
s.close()
#接收到的数据包括HTTP头和网页本身，只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header,html=data.split(b'\r\n\r\n',1)#第一个参数是分割符，后面参数是分割次数
print(header.decode('utf-8'))
#接收的数据写入文件
with open('qq.html','wb') as f:
	f.write(html)

#服务器编程
#服务器进程首先要绑定一个端口并监听来自其他客户端的连接，如果某个客户端连接过来，服务器就与该客户端建立连接，随后通信就靠这个Socket连接了
#一个socket依赖4项来确定一个socket，服务器地址，服务器端口，客服端地址，客户端端口
#服务器要响应多个客户端的请求，每个链接都需要一个新的进程或者新的线程来处理。

#编写一个简单的服务器程序，它接受客户端连接，把客户端发过来的字符串加上Hello再发过去
'''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个基于IPV4和TCP协议的socket
#监听端口
s.bind(('127.0.0.1',9999))#端口号小于1024需要管理员权限
s.listen(5)#用listen()方法监听端口，传入参数指定等待连接的最大数量
print('waiting for connection ....')
#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端连接
while True:
	sock,addr=s.accept()#接受一个新链接
	#创建新进程来处理TCP连接
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
def tcplink(sock,addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome to new world!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!' % data).encode('utf-8'))
	sock.close()
	print('connection for %s:%s closed' % addr)
'''
#写一个客户端程序
'''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect('127.0.0.1',9999)
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'yangbo',b'wenjie',b'shala']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
'''
