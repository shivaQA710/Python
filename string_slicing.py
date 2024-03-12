"""
String slicing help to accessing string within particular index
syntax : [Starting : ending]
prints including starting index  but not consider ending index 
"""

name="Hey shiva"

print(name[0:5]) #Hey s
print(name[:7]) #Hey shi
print(name[1:]) #ey shiva
print(name[:]) #Hey shiva

#  nagitive slicing
print(len(name))
print(name[-2:]) #va
print(name[0:-3]) #Hey sh
print(name[-4:-1]) #hiv