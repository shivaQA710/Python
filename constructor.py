"""
1.Special method in a class used to create and initlize an object of a class
Diffrent types of constructor
1. Default constructor
2. Parameterized constructor
"""

class emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'My {self.name}  and my {self.age}')
    
obj1 = emp("sachin",20)

print(obj1.name)
print(obj1.age)
obj1.display()
