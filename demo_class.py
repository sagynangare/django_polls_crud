class Test:
	
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return str(self.a)

obj=Test(10,20)
print(obj)
		