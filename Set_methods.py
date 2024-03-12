"""
Sets are unordered collection of data items
Sets are unchangeable, meaning you cannot change items of the set once created
because of above reason cant be accessable by index
Set help to get unique values
Represent using {}
empty set can be done by a = set() // if you do {} - > this is a dict

set having below built in function
"""

# union() and update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3) # without repeting common elements pic
cities.update(cities2) # adding cites2 to cites 

# intersection and intersection_update()
cities3 = cities.intersection(cities2) # common elemetns from both

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)  # intersection  + update citees

# symmetric_difference and symmetric_difference_update():
"""
 methods prints only items that are not similar to both the sets
  symmetric_difference_update() : update after symmetric_difference
"""

#  difference() and difference_update():
"""
 methods prints only items that are only present in the original set and not in both the sets
"""

# isdisjoint(): items of given set are present in another set
# issuperset():  items of a particular set are present in the original set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi","Seoul", "Kabul"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
# issubset(): all the items of the original set are present in the particular set
# add()  single item to the set use the add()
# update()
# remove()/discard()
# pop remove last item
# del delete the set


