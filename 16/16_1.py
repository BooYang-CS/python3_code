#python有个接口用于web处理，WSGI Web Server Gateway Interface
def application(environ,start_response):
	start_response('200 OK',[('Content-type','text/html')])#发送了Header,并且只能发送一次，也就是只能调用一次start_response()函数。
	#start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header,每个Header用一个包含两个str的tuple表示
	return [b'<h1>Hello,web!</h1>']#将作为HTTP响应的Body发送给浏览器
#application()函数就是WSGI标准的一个HTTP处理函数，它接收两个参数
#1.environ：一个包含所有HTTP请求信息的dict对象
#2.start_response:一个发送HTTP响应的函数
#有了WSGI,如何从environ这个dict对象拿到HTTP请求信息，然后够着HTML,通过start_response()发送Header，最后返回body
#application()函数必须由WSGI服务器来调用。python内置了一个WSGI服务器，他是用纯python编写的WSGI服务器参考实现的。

#HTTP请求的所有输入信息都可以通过environ获得，HTTP响应输出都可以通过start_response()加上函数返回值作为body。
'''
hello.py中有自己定义的application函数，server.py负责启动WSGI服务器，加载application函数。
浏览器输入网址，浏览器向WSGI服务器发送HTTP请求，WSGI服务器加载application函数，其中HTTP请求的输入信息可以通过
application()函数中的environ获取，application()函数中的start_response()加上函数返回值作为body.
'''