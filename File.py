"""
File is for store the data or information
Modes in file 
1.read(r) - > Read the file 
2.wirte (W)  - >it will replace privous text and add new text
3.append (a) - > append at last or updated on privious text 
4.create (x) -> 
"""

# Read file
# file = open("Python\\text.txt","r")
# print(file.read())

file = open("Python\\text.txt","a")
file.write("Hello world..11")
file.close()