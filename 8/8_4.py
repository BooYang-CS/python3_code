#序列化
#在程序运行的过程中，所有的变量都在内存中，比如，定义一个dict
d=dict(name='bob',age=20,score=90)
#在内存中可以随时修改变量，但是一旦程序结束，变量所占用内存被系统回收，如果没有修改后的变量存储到磁盘上，下次运行程序时，变量初始化不变。
#把变量从内存中变成可存储或者传输的过程称之为序列化。python中叫picking
#序列化之后，就可以把序列化的内容写入磁盘，或者通过网络传输到别的机器上。
#把变量内容从序列化的对象重新读到内存里称之为反序列化。即unpicking
#python提供pickle模块来实现序列化
import pickle
d=dict(name='bob',age=80,score=98)
print(pickle.dumps(d))
#pickdle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f=open('dump.txt','wb')#二进制写入，如果没有该文件，会创建一个文件
pickle.dump(d,f)
f.close()
#打开dump.txt是一堆乱码的内容，这些都是python保存的对象内部信息
'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象。
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
'''
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)
#这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已
#pickle只能用于python，并且不同版本的python彼此都不兼容，因此，只能用pickle保存那些不重要的东西

#JSON
#如果我们要在不同的变成语言之间传递对象，就必须把对象序列化为标准格式。比如xml,但是更好的方法是JSON.
#JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便存储到磁盘或者通过网络传输，并且比XML更快，而且可以直接在WEB页面读取，非常方便
#JSON表示的对象就是标准的JavaScript语言的对象，JSON和python内置的数据类型对应如下：
'''
JSON类型	Python类型
{}			dict
[]			list
"string"	str
1234.56		int或float
true/false	True/False
null		None
'''
#python内置的json模块提供了非常完善的python对象到JSON格式的转换。
import json
d=dict(name='bob',age=20,score=98)
print(json.dumps(d))#{"name":"bob","score":98,"age":20}
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
#要把JSON反序列化为python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str='{"name":"bob","score":98,"age":20}'
print(json.loads(json_str))#{'name':'bob','score':98,'age':20},具体的变量顺序可能每次运行结果都不一样
#JSON标准规定JSON编码是UTF—8,所以我们总是能正确在python的str和JSON字符串之间转换

#JSON进阶
#python的dict对象()可以直接序列化为JSON的{},不过很多时候更喜欢用class表示对象，比如定义Student类，然后序列化
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('bob',29,89)
#print(json.dumps(s))#直接这样将一个对象序列化会报错。
#dumps()方法还提供了一大堆可选参数，这些参数让我们来定制JSON序列化。
#可以参数default就是把任意一个对象变成一个可序列化JSON对象，我们只需要为student类专门写一个转换函数，在把函数传递进去
def student2dict(std):
	return {'name':std.name,'age':std.age,'score':std.score}
#这样Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s,default=student2dict))#成功的将一个对象序列化
#如果每次都要写student2dict函数，会比较麻烦，这里有简单方法
print(json.dumps(s,default=lambda obj:obj.__dict__))
#因为class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。但是定义__slots__的class除外，因为它限制了属性
#要把JSON反序列化为以一个Student对象实例，loads()方法首先转换出一个dict对象，然后传入object_hook函数负责把dict转换成Student实例
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])#为Student类传入三个参数，初始化实例对象
json_str='{"score":89,"name":"bob","age":23}'
print(json.loads(json_str,object_hook=dict2student))

'''
json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''
