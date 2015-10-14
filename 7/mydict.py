class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):#用__getattr__()得到对象的属性
		try:
			return self[key]
		except KeyError:
			raise AttributeError("'Dict' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):#给属性设置关键字
		self[key]=value