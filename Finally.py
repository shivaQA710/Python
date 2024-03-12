"""
Finally block execute every time in execption handling. this mainly used to do clean up activity
"""

try:
    a=1/0
except ZeroDivisionError:
    print("number ends in infinete")
finally:
    print("Finally execute every time")