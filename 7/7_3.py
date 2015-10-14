#单元测试
#单元测试就是用来对一个模块，一个函数或者一个类来进行正确性检验的测试工作
"""
比如函数abs(),我们可以编写以下几个测试：
1.输入正数，比如1,1.2,0.99,期待返回值与输入相同
2.输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反
3.输入0，期待返回0
4.输入非数值，比如None,[],{},期待输出TypeError
把上面的测试用例放到测试模块里，就是一个完整的单元测试
如果单元测试通过，说明测试的这个函数能够正常工作。否则，有bug或者错误
使用单元测试可以确保一个程序模块的行为符合我们设计的测试用例。
"""
d={'a':1,'b':2}
print(d['a'])
print(d.get('b'))
#编写一个Dict类，这个类的行为和dict一致。但是可以通过属性来访问。mydict.py如下
class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):#用__getattr__()得到对象的属性
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Dict' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):#给属性设置关键字
		self[key]=value
#为了编写单元测试，需要引入python自带的unittest模块，mydict_test.py如下
import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty
#编写单元测试时，需要编写一个测试类，从unittest.TestCase继承，以test开头的方法就是测试方法，否则不被认为ishi测试方法，测试的时候不被执行
#由于unittest.TestCase提供了很多内置的条件，只要调用这些方法就可以断言输出是不是我们所期望的
#最常用的断言就是assertEqual()
#self.assertEqual(abs(-1),1)
#另一种断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
'''
with self.assertRaises(KeyError):
	value=d['empty']
'''
#通过d.empty访问不存在的key时，我们期待抛出AttributeError
'''
with self.assertRaises(AttributeError):
	value=d.empty
'''
#运行单元测试
#最简单的运行方式就是在mydict_test.py的最后加上两行代码:
'''
if __name__='__main__':
	unittest.main()
'''
#这样就可以把mydict_test.py当作正常的python脚本运行：python mydict_test.py
#另一种方法是在命令行通过参数-m unittest直接运行单元测试:
#python -m unittest mydict_test
#推荐这种做法，可以一次批量运行很多单元测试，并且可以用工具来自动运行

#setUp与tearDown
#可以在单元测试中编写两个特殊setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法前后分别被执行
#当测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
#这样不必再每个测试方法中重复相同的代码
'''
class TestDict(unittest.TestCase):
	def setUp(self):
		print('setUp....')
	def tearDown(self):
		print('tearDown...')
'''
#单元测试通过了并不意味着程序没有bug了，但是不通过程序肯定有bug
