"""
Local var = confined to same class or same function 
Global : confined to throught the program
"""

global_var=10

def Display():
    local_var=5
    print(global_var)
    print(local_var)

print(global_var)
print(local_var) #not accessable

