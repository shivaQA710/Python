"""
Function that allows you to loop over a sequence  and get index and value of each element at a same time
"""


f =['apple','banana','mango']
for index,value in enumerate(f):
    # print(index,value)
    print(f'{index}:{value}')

# Changing the satrt index 

f =['apple','banana','mango']
for index,value in enumerate(f,start=1):
    print(index,value)

