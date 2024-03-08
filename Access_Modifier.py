"""
Public access modifier
Private access modifier
Protected access modifier

private modifier indicate by = __varname

"""

class emp:

    def __init__(self):
        self.__name ="Sachin"
    
    def _funName(self):      
        return "employeeFun"

e = emp()
print(e._emp__name)

print(e._funName())     

