#server.py负责启动WSGI服务器，加载application()函数
from wsgiref.simple_server import make_server
#导入自己编写的application函数
from hello import application
#创建一个服务器，ip地址为空，端口号8000，处理函数是application
httpd=make_server('',8000,application)
print('Servering HTTP on part 8000....')
httpd.serve_forever()