age=20
if age>=19:
	print("you age is ",age)
	print('adult')
else:
	print("you age is ",age)
	print("teenager")

age=10
if age>19:
	print("audlt")
elif age>8:
	print("teenager")
else:
	print("kid")
#if语句是从上往下判断，如果在某个判断是True，则执行对应的语句后，就会忽略掉剩下的elif和else
age=20
if age>=6:
	print("teenager")
elif age>18:
	print("adult")
else:
	print("kid")
#input()输入问题
s=input('birth:')#input()返回的数据类型是str，str不能直接和整数比较，Python提供int()函数进行转换
birth=int(s)
if birth<2000:
	print('00前')
else:
	print('00后')
#循环,Python循环有两种，一种是for..in循环，依次把list和tuple的元素迭代出来
names=['bobo','lili','gejing']
for name in names:
	print(name)
#for x in ...循环就是把每一个元素带入变量，然后执行语句
sum=0
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum=sum+x
print('sum=',sum)
#range()函数可以生成一个整数序列，在通过list()函数可以转换成list,range(i)函数产生的序列是从0开始小于i的整数
print(list(range(10)))
sum=0
for x in(list(range(100))):#也可以直接写成for x in range(100):
	sum=sum+x
print('sum=',sum)
#while循环
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print('sum=',sum)