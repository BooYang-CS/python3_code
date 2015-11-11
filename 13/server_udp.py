import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',8888))
#不需要使用listen()方法，而是直接接收来自任何客户端的数据
print('Bind UDP on 8888...')
while True:
	data,addr=s.recvfrom(1024)
	print('received from %s:%s' % addr)
	s.sendto(b'hello,%s!' % data,addr)