#1. 使用枚举类
from enum import Enum
Month=Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
#获得Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
print(Month.Feb)
#value属性怎是自动赋给成员的int常量，默认从1开始计数
#如果需要精确的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum,unique
@unique
class Weekday(Enum):
	Sun=0#Sun的value值设定为0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
# @unique装饰器可以帮助检查保证没有重复值
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1==Weekday.Mon)
print(Weekday(1))
#print(Weekday(7))#7不是有效的value值
for name,member in Weekday.__members__.items():
	print(name,'=>',member)
#既可以用成员名引用枚举常量，又可以直接根据value的值获得枚举效果

#2. 使用元类
#2.1 type()
#动态语言和静态语言的最大不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#type()函数可以查看一个类型或变量的类型.
class Hello(object):
	def hello(self,name='world'):
		print('Hello,%s.' % name)
h=Hello()
h.hello()
print(type(Hello))
print(type(h))
#Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
#type()函数既可以返回一个对象的类型，又可以创建出新的类型。比如，通过type()函数创建Hello类。
def fn(self,name='world'):#先定义函数,也可以当作类的方法
	print('Hello,%s.' % name)
Hello=type('Hello',(object,),dict(hello=fn))#创建Hello class
h1=Hello()
h1.hello()
print(type(Hello))
print(type(h))
'''
创建一个class对象，type()函数依次传入3个参数：
1.class的名称
2.继承的父类集合，注意python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法(object,).
3.class的方法名称与函数绑定，这里把函数fn绑定到方法名hello上.
通过type()函数创建的类和直接写class是完全一样的，因为python解释器遇到class时，仅仅是扫描一下class定义的语法
然后调用type()函数创建class
'''
#2.2 metaclass 一般很难用到
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
#metaclass直译为元类，当我们定义类后，就可以根据这个类创建出实例。即先定义类，然后创建类
#但是如果想创建类，就必须根据metaclass创建类，所以：先定义metaclass，然后创建类
#先定义metaclass，就可以创建类，最后创建实例。
#metaclass允许创建类或修改类，换句话说，可以把类看成metaclass创建出来的"实例"

#metaclass是类的模板，所以必须从'type'类型派生
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']=lambda self,value:self.append(value)
		attrs['add2']=lambda self,value:self.append(value*2)
		return type.__new__(cls,name,bases,attrs)
#先定义ListMetaclass，metaclass的类名总是以Metaclass结尾，以便清楚的表示这是一个metaclass
#有了ListMetaclass,在定义类的时候还要指示使用ListMetaclass来制定类，传入关键字参数metaclass
class Mylist(list,metaclass=ListMetaclass):
	pass
#python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建。
'''
__new__()方法接收到的参数依次是：
1.当前准备创建的类的对象
2.类的名字
3.类继承的父类集合
4.类的方法集合 attrs['add','plus']=lambda self,value:self.append(value),lambda self,value:append(vlaue*2)
'''
L=Mylist()
L.add(1)
print(L)
L.add(2)
print(L)
L.add2(3)
print(L)
#而普通的list没有add方法
L2=list()
#L2.add(1)
#动态修改有什么意义，一般情况下，是不需要使用metaclass的。但也有需要的时候
'''
ORM即对象-关系映射，即把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，
不用直接操作SQL语句
要编写一个ORM框架，所有类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
#先把调用接口写出来，比如使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User.
class User(Model):
	#定义类的属性到列的映射
	id=IntegerField('id')
	name=StringField('username')
	email=StringField('email')
	password=StringField('password')
#创建一个实例
#u=User(id=1234,name='bibi',email='test@123.com',password='my_pwd')
#保存到数据库
#u.save()
#父类Model和属性类型StringField,IntegerField是由ORM框架提供。save()方法全部由metaclass自动完成。
#下面按照上面的接口来实现该ORM
#首先定义Filed类，它负责保存数据库表的字段名和字段类型
'''
class Field(object):
	def __init__(self,name,column_type):
		self.name=name
		self.column_type=column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__,self.name)
#在Field的基础上，进一步定义各种类型的Field，比如StringFiled,IntegerField
class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')
#编写复杂的ModelMetaclass
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()