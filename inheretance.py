"""
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

Types of inheritance:
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance

"""


class Parent:
    p_value=10
    def p(self):
        print("Value in parent class ",self.p_value)

class child(Parent):
    c_value=5
    def c(self):
        print("Value in parent class ",self.c_value)

child_instance = child()

# Now print the class attribute directly
print(child_instance.p_value)
print(child_instance.p())

    
    