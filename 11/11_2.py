#collections
#collections是python内建的一个集合模块，提供了许多有用的集合类

#1.namedtuple
p=(1,2)#用一个元组tuple表示不变集合，很难看出这个tuple是用来表示一个坐标的
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(p[1])#但是p还是一个元组tuple只不过是一个定制版的tuple
print(isinstance(p,tuple))
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并规定tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
#这样可以用namedtuple可以定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用。
#类似地，也可以用坐标半径表示一个园
Circle=namedtuple('Circle',['x','y','r'])

#2.deque
#使用list存储数据时，按索引访问数据很快，但是插入和删除就很慢，因为list是线性存储，数据量大时，插入和删除效率很低
#deque是为了高效实现插入和删除的双向列表，适合用于队列和栈
from collections import deque
q=deque(['a','b','v'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()#删除尾部元素
q.popleft()#删除头部元素
print(q)
#deque实现 list的append()和pop()，还支持appendleft()和popleft()，这样可以非常高效的向头部和尾部添加或删除元素。

#3.defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])#key2不存在，返回默认值 N/A
#defaultdict的其他行为跟dict是完全一样的

#4.OrderedDict
#使用dict时，Key是无序的，在对dict做迭代时，我们无法确定key的顺序。
#要保持key的顺序，可以使用OrderedDict
from collections import OrderedDict
d=dict([('a',1),('f',3),('t',5)])
print(d)#dict的key是无序的
od=OrderedDict([('a',1),('c',4),('r',0)])
print(od)#OrderedDict的key是有序的
#OrderedDict的key会按照插入的顺序排列，而不是Key本身排序
od1=OrderedDict()
od1['x']=1
od1['r']=2
od1['w']=4
print(list(od1.keys()))#按照插入的Key的顺序返回,将keys按list格式返回

#5. Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'Programming':
	c[ch]=c[ch]+1
print(c)
print(c)

