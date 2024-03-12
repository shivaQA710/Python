"""
when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
Walrus Operator is represented by the := 
"""

# numbers = [1, 2, 3, 4, 5,1]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())


names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")
