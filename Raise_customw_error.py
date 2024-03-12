"""
Handling exeption by custom exception
"""
a =int(input("enter any value between 5 -10 "))

if(a<5 or a>10):
    raise ValueError("value should be between 5 -10 ")