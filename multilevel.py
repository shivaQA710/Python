"""
multiple parent classes in the class definition, separated by commas.
"""


class Animal:
    animal="common animal"

    def animalFunc(self):
        print("Animal function")

class Dog(Animal):
    dog="dog"

    def dogFunc(self):
        print("Dog function")

class Run(Dog):
    dogRun="40kmph"

    def dogRunFunc(self):
        print("dogRun fucntion")


r =Run()
print(r.animalFunc())