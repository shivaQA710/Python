"""

Function is set of particular instruction performing specific task 
use : reuse code increse performance 

default argument 
keywork argument
variable length arguments
required arguments
"""
# without parameter 
def demoFun():
    print("Demo functions")


demoFun()

# with parameter
def add(a ,b):
    return a+b

print(add(1,2))

# with optional parameter

def addOptional(a,b=1):
    return a+b

print(addOptional(5)) # 1+5 =6


def avarage(*numbers):
    sum =0 
    for i in numbers:
        sum =sum+i
        print("avarage = ",sum)