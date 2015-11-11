import socket,threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个基于IPV4和TCP协议的socket
#监听端口
s.bind(('127.0.0.1',9999))#端口号小于1024需要管理员权限
s.listen(5)#用listen()方法监听端口，传入参数指定等待连接的最大数量
print('waiting for connection ....')
#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端连接
def tcplink(sock,addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome to new world!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection for %s:%s closed' % addr)
while True:
	sock,addr=s.accept()#接受一个新链接
	#创建新进程来处理TCP连接
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()