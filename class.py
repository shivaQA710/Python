"""
class : A class is a blueprint or a template for creating objects, providing initial values for state
object : Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
self : self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class

"""
class emp:
    name="sachin"
    age =28

    def display(self):
        print(self.name,self.age)


obj1=emp()
print(obj1.age)
print(obj1.name)
obj1.display()


