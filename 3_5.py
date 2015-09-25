#迭代器
'''
直接作用于for循环的数据类型有以下几种：
一种是集合数据类型，比如list，tuple，dict，set，str等
一种是generator，包括生成器和带yield的generator function
可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance()判断一个对象是否是Iterable对象
'''
from collections import Iterable 
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(111,Iterable))
'''
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
直到最后抛出StopIteration错误。
可以被next()函数调用并不断返回下一个值得对象称为迭代器：Iterator
可以使用isinstance()判断一个对象是否是Iterator对象
'''
from collections import Iterator 
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance(111,Iterator))
#只有生成器是Iterator对象，但list，dict，str虽然是Iterable，却不是Iterator
#把list，dict，str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
'''
为什么list，dict，str等数据类型不是Iterator,因为python的Iterator对象表示
一个数据流，iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时，抛出
StopIteration错误。可以把数据流看成一个有序序列，但是我们不能提前知道序列的
长度，只有不断通过next()函数实现按需计算下一个数据，所以iterator的计算是惰性的
，只有在需要时返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而list是永远不会存储全体自然数的
'''
#python的for循环本质上就是通过不断调用next()函数实现的。