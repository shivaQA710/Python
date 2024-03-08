"""
They are a way to extend the functionality of a function or method without modifying its source code.
A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
The new function is often referred to as a "decorated" function
"""
def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

hello()
# @greet
# def add(a, b):
#   print(a+b)
  

# add(1, 2)