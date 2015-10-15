#文档测试
"""
def abs(n):
	'''
	Function to get absolute value of number.
	Example:
	>>>abs(1)
	1
	>>>abs(-1)
	1
	>>>abs(0)
	0
	'''
	return n if n>=0 else(-n)
"""
#当我们编写代码时，如果写上述的注释,无疑更明确地告诉函数的调用者该函数的期望输入和输出
#并且，python内置的"文档测试（doctest）"模块可以值姐提取注释中的代码并执行
#doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确。
#只要测试异常的时候，可以用....表示中间一大段烦人的输出
#用doctest来测试上次编写的Dict类
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()