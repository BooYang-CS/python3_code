#-*- coding:utf-8 -*-
#nslookup可以指定查询的类型，可以查到DNS记录的生存时间还可以指定使用哪个DNS服务器进行解释。
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
#注意subprocess是一个系统模块，故自定义文件不能定义成subprocess.py否者会出错
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'setq=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:',p.returncode)