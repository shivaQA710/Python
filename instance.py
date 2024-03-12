"""
Class variable : defined in class levl can be accessed throught the class 
instance variable : defined and declare by instance 

"""

class employee:

    workCompany ="Beta"

    def __init__(self,id,name,age):
        self.name=name
        self.id =id
        self.age=age
    
    def showDetails(self):

        print(f"my Name is {self.name} and my id is {self.id} and i am {self.age} old . i am working at {self.workCompany}")

    

emp1= employee(1,"sachin",25)
emp1.name="shivanagouda"
emp1.showDetails()

emp2= employee(2,"sachin2",222)
emp2.workCompany ="FB"
emp2.showDetails()


