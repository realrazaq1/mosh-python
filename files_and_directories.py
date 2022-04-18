# pathlib: module that contains classes we can use to work with directories and files
# then create a path object to reference a file or directory on our computer
# we can use an Absolute path or Relative path
# Relative path: a path starting from the current directory
# Exp: ./ecommerce
# Absolute path: we start from the root of our hard disk
# Exp: C:\Program Files\Microsoft
# In windows we use \ to build paths
# On Mac and Linux we use / e.g /usr/local/bin
# Path() - if you don't pass an argument, it will reference the current directory. We can add a string which could be a file or directory
# Path() - returns a path object
# the path object has some interesting methods we can use

# import pathlib
from pathlib import Path

# path = Path("ecommerce")
# path = Path("ecommerce1")
# check if a path exist
# print(path.exists())

# create a folder
# path = Path("emails")
# if not path.exists():
#     path.mkdir()
#     print("folder created...")
# else:
#     print("folder already exist")

# delete folder
# path = Path("emails")
# if path.exists():
#     path.rmdir()
#     print("folder deleted...")
# else:
#     print("folder doesnt exist")
#     print("creating folder....")
#     path.mkdir()

# we can also find all the files and folders in a given path. useful if u want to write a program that automate something. for example, you can loop through all the spreadsheets in a folder, open them and process them
# *.* - all the files
# *.py - all python files
# *.xls - all excel files
# Read about - generator object
# we can loop thru generator objects
# path = Path()
# for file in path.glob("*.py"):
#     print(file)

# all the files and folders in the current path
path = Path()
for file in path.glob("*"):
    print(file)
