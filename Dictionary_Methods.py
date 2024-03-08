# update()
"""
updates the value of the key provided to it if the item already exists in the dictionary, 
else it creates a new key-value pair.
"""
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# clear(): The clear() method removes all the items from the list.
info.clear()

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# popitem(): opitem() method removes the last key-value pair from the dictionary
# del: we can also use the del keyword to remove a dictionary item


