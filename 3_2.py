#迭代
'''
如果给定一个list或则tuple，可以同过for循环来遍历这个list或tuple，这种
遍历称为迭代
'''
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
#dict的存储方式不是按照list的方式顺序排列，所以迭代出来的结果顺序很可能不一样
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,v)
#同时迭代key和value，和只迭代值
#字符串也可以是迭代对象
for ch in 'ABC':
	print(ch)
#判断一个额对象是否是可迭代对象，通过collections模块的iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
#判断字符串，list，和整数是否是可迭代对象，整数不是可迭代对象
'''
Python内置函数enumerate函数可以把一个list变成索引-元素对，这样
就可以在for循环中同时迭代索引和元素本身
'''
for i,value in enumerate(['A','B','C']):
	print(i,value)
#for循环里引用两个变量
for x,y in[(1,2),(2,3),(4,6)]:
	print(x,y)
'''
只要符合迭代条件，就可以使用for循环
'''