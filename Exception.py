"""
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
Exception handling deals with these events to avoid the program or system crashing, and without this process,
exceptions would disrupt the normal operation of a program.
"""

# Python try...except

try:
    a = int(input("Enter a number  : "))
    print("Number ",a)
except:
    print("Invalid input...")