"""
class inherits properties and behaviors from a single parent class. 
This is the simplest and most common form of inheritance.
"""


class Animal:
    animal="common animal"

    def animalFunc(self):
        print("Animal function")

class Dog(Animal):
    dog="dog"

    def dogFunc(self):
        print("Dog function")

d = Dog()
print(d.animal)
print(d.animalFunc())
