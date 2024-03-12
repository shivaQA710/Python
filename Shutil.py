"""
Shutil is a Python module that provides a higher level interface for working with file and directories.
 It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. In this rep
"""


import shutil

# Copying a file
shutil.copy("src.txt", "dst.txt")

# Copying a directory
shutil.copytree("src_dir", "dst_dir")

# Moving a file
shutil.move("src.txt", "dst.txt")

# Deleting a directory
shutil.rmtree("dir")