"""
Getters in Python are methods that are used to access the values of an object's properties
 They are used to return the value of a specific property, and are typically defined using the @property decorator
Setters

we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter
 """

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


# obj1 = MyClass(10)
# obj1.value = 20
# print(obj1.value)


class emp:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def getValue(self):
        return self.name,self.age
    
    
    @getValue.setter
    def getValue(self,name,age):
        self.name=name
        self.age=age
    

e = emp("Sachin",28)
e.name="shiva"
e.age=200
print(e.getValue)
