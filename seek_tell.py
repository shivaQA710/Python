""""
Seek() -> allows you to move the current postion within a file to a specific point 2, you can move either forward or backword form the current postion
tell() -> returns the current postion within the file,use to keep track of your location within the file
"""

with open("Python\\text.txt","r") as f:
    data =f.read(10)
    current_postion =f.tell()
    f.seek(current_postion)
    print(data)
    print(current_postion)

# with open("Python\\text.txt","w") as f:
#   f.truncate(5)