#递归函数
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(3))
print(fact(20))
#递归函数要注意防止栈溢出，每当进入一个函数调用，栈会增加一层，每当函数返回，栈会减一层
#解决递归调用栈溢出的方法是通过尾递归优化。
#尾递归是指在函数返回的时候，调用自身，并且return语句不能包含表达式。这样是递归本身无论调用多少次，都只占用一个栈帧
def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
print(fact(10))
print(fact(100))
#尾递归调用时，如果做了优化，栈不会增长，无论调用多少次都不会导致栈溢出
#但是大多数语言都没有针对尾递归做优化，Python也没有，所以还是会栈溢出
#递归函数练习，汉诺塔
def move(n,a,b,c):#n表示第一个柱子A的盘子的数量
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(3,'A','B','C')
