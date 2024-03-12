"""
String methods

1. strings are immutable in nature

"""


a="i HarraY!!!!!!Harray!!!"
print(a.upper()) # convert str to upper
print(a.lower()) # convert str to lower
print(a.rstrip("!")) # remove particular limiter
print(a.replace("HarraY","sacHIN")) # replace by arg2 to arg1
print(a.count("HarraY")) # count particular word
print(a.endswith("!!!")) # true boolian value 
print(a.islower()) # true if a is lower

b="good Morning"
print(b.capitalize()) # capitalize the first charater
print(b.center(50)) # Move sting to center by 50 space adding behind

str="welcome to the console"
print(str.endswith("to",4,10)) #withing 4 to 10 "to" is coming or not 
print(str.find("to")) # give the index of first occarance

str1="12Abc\n"
print(str1.isalnum()) # check it contain only a-z , A-Z ,0-9 [not consider special cheretor]
print(str1.isalpha()) # check it contain only a-z , A-Z 
print(str1.isspace()) # true if space
print(str1.isprintable()) # false beause \n wont print simmilarly lt
print(str1.swapcase()) # conver lowercase to upper and vice versa
print(str1.startswith("12")) # true if- satrts with 12
print(str1.endswith()) #c



