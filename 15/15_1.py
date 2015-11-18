#SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
#Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
"""
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
"""
#Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
#由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

#我们在Python交互式命令行实践一下：
"""
# 导入SQLite驱动:
>>> import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
>>> conn = sqlite3.connect('test.db')
# 创建一个Cursor:
>>> cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# 继续执行一条SQL语句，插入一条记录:
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
>>> cursor.rowcount
1
# 关闭Cursor:
>>> cursor.close()
# 提交事务:
>>> conn.commit()
# 关闭Connection:
>>> conn.close()
我们再试试查询记录：

>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
# 执行查询语句:
>>> cursor.execute('select * from user where id=?', '1')
<sqlite3.Cursor object at 0x10f8aa340>
# 获得查询结果集:
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
>>> cursor.close()
>>> conn.close()
"""
#使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
#使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
#使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
#如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
#cursor.execute('select * from user where id=?', '1')

#小结

#在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

"""
练习:在Sqlite中根据分数查找指定的名字
"""
import os,sqlite3
db_file=os.path.join(os.path.dirname(__file__),'test1.db')
if os.path.isfile(db_file):
	os.remove(db_file)
conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bobo',85)")
cursor.execute(r"insert into user values ('A-003','Gogo',78)")
cursor.execute(r"insert into user values ('A-004','Ghyu',68)")
cursor.close()
conn.commit()
conn.close()
def get_score_in(low,high):
	cursor.execute('select user.name from user where score between ? and ? order by score' ,(low,high))
	values=cursor.fetchall()
	#print(values)
	l_values=list(map(lambda x:x[0],values))#map是将传入的函数依次作用到序列的每个元素，并把新的结果作为Iterator返回，这里只取元组的第一元素
	#print(map(lambda x:x[0],values))
	return l_values
conn=sqlite3.connect('test1.db')
cursor=conn.cursor()
print(get_score_in(60,70))
print(get_score_in(70,90))
print(get_score_in(60,100))
cursor.close()
conn.close()
#注意将组成元素为元组的list转换成组成元素为单个值的list