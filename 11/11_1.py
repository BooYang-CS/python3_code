#python内建模块之datetime
#1.获取当前时间和日期
from datetime import datetime
now=datetime.now()#获取当前datetime
print(now)
print(type(now))
#datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
#如果仅导入import datetime,则必须引用全名datetime.datetime
#datetime.now()返回当前日期和时间，其类型是datetime

#2. 获取指定日期和时间
#可以直接用参数构造一个datetime,指定某个日期和时间
from datetime import datetime
dt=datetime(2015,10,23,12,33)#用指定日期时间创建datetime
print(dt)

#3.datetime转换为timestamp
'''
在计算机中，时间实际上是用数字表示的，把1970年1月1日00:00:00 UTC+00:00时区称为epoch time,记为0(1970年以前的时间timestamp为负数)，
当前时间就是相对于epoch time的秒数，称为timestamp.
timestamp=0=1970-1-1 00:00:00 UTC+ 0:00
对应的北京时间:
timestamp=0=1970-1-1 08:00:00 UTC+ 8:00
timestamp的值和时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是
为什么计算机存储的当前时间是以timestamp表示，因为全球各地的计算机的任意时刻的timestamp都是完全相同的。
'''
#把一个datetime类型转换为timestamp只需要简单的调用timestamp()方法
from datetime import datetime
dt=datetime(2015,10,24,16,37)#用指定日期时间创建datetime
print(dt.timestamp())#把timestamp转换为datetime
#1445675820.0  #是总秒数

#4.timestamp转换为datetime
#要把timestamp转换为datetime,使用datetime提供的fromtimestamp()方法
from datetime import datetime
t=1445675820.0
print(datetime.fromtimestamp(t))
#timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的，上述转换是在timestamp和本地时间做转换。
#本地时间是指当前操作系统设定的时区，例如北京时区则本地时间:2015-10-24 16:37:00
#timestamp也可以直接被转换到UTC标准时区的时间
from datetime import datetime
t=1445675820.0
print(datetime.fromtimestamp(t))#本地时间，是北京时区时间
print(datetime.utcfromtimestamp(t))#UTC时间，是格林威治时间

#5.str转换为datetime
#很多时候用户输入的日期和时间是字符串，要处理时间和日期，需要把str转换成datetime,转换方法是通过datetime.strptime()实现
from datetime import datetime
cday=datetime.strptime('2015-10-24 16:54:46','%Y-%m-%d %H:%M:%S')
print(cday)#后面的字符串规定日期的格式，转换后的datetime是没有时区信息的

#6. datetime转换为str
#如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str,转换方法是通过strftime()实现的
from datetime import datetime
now=datetime.now()
print(now)
print(now.strftime('%a,%b %d %H:%M:%S'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#7.datetime加减
#对日期和时间进行加减实际上就是把datetime往后或则往前计算，得到新的datetime.可以直接使用+和-符号，不过要导入timedelta这个类
from datetime import datetime,timedelta
now=datetime.now()
print(now)
print(now+timedelta(hours=10))
print(now-timedelta(days=2))
print(now+timedelta(days=1,hours=10))
#使用timedelta可以很容易计算时间差

#8.本地时间转换为UTC时间
#本地时间是系统设定时区的时间，北京是UTC+8:00时区的时间，而UTC时间是指UTC+0:00时间
#一个datetime类型有一个时区属性tzinfo,但是默认是None，所以无法区分这个datetime到底是哪个时区，除非给datetime设定时区
from datetime import datetime,timedelta,timezone
tz_utc_8=timezone(timedelta(hours=8))#创建时区UTC+8:00
now=datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)#强制设置为UTC+8:00
print(dt)
#刚好系统时区恰好是UTC+8:00，上述强制设置UTC时区代码是正确的，否则是错误的

#9.时区转换
#首先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)#拿到utc时间，并强制设置为时区UTC+0:00
print(utc_dt)
#astimezone()强制将时区设为北京时区
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
#astimezone()强制将时区设为东京市区
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
#astimezone()将bj_dt转换时区为东京时区
tokyo2_dt=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo2_dt)
'''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
'''
#datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

'''
练习：
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
请编写一个函数将其转换为timestamp。
'''
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    re_dt = re.compile(r'^\d{4}-[1-9]|1[12]-[1-9]|[12]\d|3[01]\s\d|[01]\d|2[0-4]:\d|[1-5]\d|60:\d|[1-5]\d|60$')
    re_tz = re.compile(r'^UTC[\+\-](\d|[01]\d|2[0-4]):(\d|[0-5]\d|60)$')
    if re_dt.match(dt_str) and re_tz.match(tz_str):
        dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
        tz_num = int(re_tz.match(tz_str).group(1))
        tz_utc = timezone(timedelta(hours = tz_num))
        dt = dt.replace(tzinfo = tz_utc)
        return dt.timestamp()
t1=to_timestamp('2015-10-23 05:29:10','UTC+07:00')
print(t1)