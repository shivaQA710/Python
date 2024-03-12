"""
static methods belongs to class not instance    

"""

class calculator:


    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod    
    def mult(a,b):
        return a*b

e = calculator()
print(e.add(1,2))
print(e.mult(2,2))
