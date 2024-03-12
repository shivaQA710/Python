"""
you can create a generator by using the yield statement in a function
he yield statement returns a value from the generator and suspends the execution of the function until the next value is requested
The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.
"""


def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))

print("12222222222222")

print(next(gen))
print("12222222222222")
print(next(gen))
print("12222222222222")

# Output:
# 0
# 1
# 2
# 3
# 4