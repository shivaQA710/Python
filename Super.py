"""
The super() keyword in Python is used to refer to the parent class. 
It is especially useful when a class inherits from multiple parent classes and 
you want to call a method from one of the parent classes.    
"""

class parent:
    a = 100
    def parentfun(self):
        print("Parent function")
    
class child(parent):

    def childFun(self):
        print("Child class")

    def supercall(self):
        super().parentfun()
        print("x :",super().a)
        print("calling super")


c = child()
# c.parentfun()
# c.childFun()
c.supercall()