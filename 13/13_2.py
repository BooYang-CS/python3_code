#UDP编程
#UDP是面向无连接的协议
#使用UDP时无需建立连接，只需要知道对方IP地址和端口号，就可以直接发送数据包，但是是不可靠的
#服务器端
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
#recvfrom()方法返回数据和客户端的地址与端口，服务器收到数据后就可以直接调用sendto()就可以把数据用UDP发送给客户端
#客户端
'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'yangbo',b'wenjie',b'shala']:
	s.sendto(data,('127.0.0.1',8888))
	print(s.recv(1024).decode('utf-8'))
s.close()
'''
