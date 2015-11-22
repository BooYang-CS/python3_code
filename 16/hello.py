def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
#从environ里读取PATH_INFO，environ是一个包含HTTP请求信息的dict对象。


