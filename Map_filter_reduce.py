"""
map:function argument is a function that is applied to each element in the iterable argument
filter : Filter is condtion .
"""
from functools import reduce


l=[1,2,3,4,5]
newl=list(map(lambda x:x*x*x,l))
print(newl)


def filterFun(a):
    return a>2

newl=list(filter(filterFun,l))
print(newl)

numbers=[1,2,3]

def mysum(x,y):
    return x+y


print(reduce(mysum,numbers))