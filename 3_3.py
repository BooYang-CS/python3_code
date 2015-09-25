'''列表生成式 List Comprehensions ，是python内置的非常简单却强大的可以用来创建list的生成式'''
print(list(range(1,11)))#创建一个简单的list，用[]表示
L=[]
for x in range(1,11):
	L.append(x*x)
print(L)
#这种循环太繁琐，可以用列表生成式来代替循环生成上面的list
print([x*x for x in range(1,11)])
print([x*x for x in range(1,22) if x%2==0])#for循环后面可以加上if判断
print([m+n for m in 'ABC' for n in "XYZ"])#两层循环实现全排列
#利用列表生成式，可以写出非常简洁的代码，例如列出当前目录下的所有文件和目录名
import os#导入os模块
print([d for d in os.listdir('.')])#os.listdir可以列出文件和目录
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)
#列表生成式，可以使用两个变量来生成list
d={'x':'1','y':'2','z':'3'}
print([k+'='+v for k,v in d.items()])#+表示字符串的拼接
L=['Hello','World','IBN','Apple']
print([s.lower() for s in L])#将一个list中所有的字符串变成小写
'''
练习:如果list中即包含字符串，有包含整数，由于非字符串类型没有lower()方法，使用isinstance函数判断一个变量是不是字符串
'''
L=['Hello','WORLD',12,'APPlE',None]
L1=[]
[L1.append(s) for s in L if isinstance(s,str)==True]
print([s.lower() for s in L1])
#或者
L2=['Hello','WORLD',12,'APPlE',None]
L3=[x.lower() for x in L1 if isinstance(x,str)]
print(L3)