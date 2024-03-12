"""
allows a subclass or child class to provide a specific implementation of a method that is 
already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, s
ame parameters or signature
"""



class Parent(): 
	

	def __init__(self): 
		self.value = "Inside Parent"
		

	def show(self): 
		print(self.value) 
		

class Child(Parent): 
	

	def __init__(self): 
		self.value = "Inside Child"
		

	def show(self): 
		print(self.value) 
		
		

obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 
