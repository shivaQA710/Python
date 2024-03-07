"""
The __dict__ attribute returns a dictionary representation of an object's attributes

"""

class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p = person("sachin",1)
print(p.__dict__)