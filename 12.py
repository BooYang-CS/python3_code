#python 图形界面
#python自带库Tkinter支持TK
#Tk是一个图新库，支持多个操作系统，使用Tcl语言开发
#编写的python代码会调用内置的Tkinter,Tkinter封装了访问Tk的接口
#Tk会调用操作系统提供的本地GUI接口，完成最终的GUI
#python代码只需要调用Tkinter提供的接口就可以了

#第一个GUI程序
from tkinter import *  #导入Tkinter包的所有内容
#从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.helloLabel=Label(self,text='Hello,world!')
		self.helloLabel.pack()#将helloLabel加入父容器
		self.quitButton=Button(self,text='Quit',command=self.quit)#定义一个按钮，文本是Quit，命令是self.quit
		self.quitButton.pack()#然后将按钮加入父容器
'''
在GUI中，每个Button，Label，输入框等，都是一个Widget(窗口小部件)。Frame则是可以容纳其他Widget的Widget，所有Widget组合起来就是一颗树。
pack()方法把Widget加入到父容器中，并实现布局。在createWidgets()方法中，创建一个Label和一个Button，当Button被点击，触发self.quit()使程序退出
'''
#实例化Application，并启动消息循环
app=Application()
#设置窗口标题
app.master.title('Hello,world!')
#主消息循环
app.mainloop()

#输入文本
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alertButton=Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	def hello(self):
		name=self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello,%s' % name)
app=Application()
app.master.title('Hello,world')
app.mainloop()
