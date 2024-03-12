"""
Tuples are immutable cant replace or cant be updated
Tuple is similar to list , but tuple cant be update 
in order to update the tuple it has to be convertted to list first

important  : tuple supports only 2 methods 1 . tup.index(number) 2. tup.count(number)

convert tuple to list and use all the inbuilt function from list 
"""
tup =(1,5,6,2,3,4,5,6)

print(tup[1])
print(tup[2:])
print(tup[:3])
print(tup[:])
print(tup[-1])


# tup[0]=100  theows an error cant change

# convert tuple to list 
l = list(tup)
print(l)