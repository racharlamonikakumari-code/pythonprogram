class A:
	print("A static block")
	def _init_(self):
		self.x=10
		print("A constructor")
	def _del_(self):
		print("A destructor ")
	
class B(A):
	print("B static block")
	def _init_(self):
		self.y=20
		super()._init_()
		print("B constructor")
	def _del_(self):
		super()._del_()
		print("B destructor ",self.x)
	
ob=B()
print(ob.__dict__)
help(B)