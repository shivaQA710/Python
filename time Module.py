"""
time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch 
"""
import time

print(time.time()) 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
