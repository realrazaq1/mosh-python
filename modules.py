# a module is simply a file with some python code
# we use modules to organize our code into multiple files
# and also makes our code reusable
# a module should contain all the related functions and classes

# import <file_name> without the extension to import a module
# we can use . to access the things in the module
# we can also import specific things from a module without importing the entire module

import converters
from converters import kg_to_lbs
from utils import find_max

print(kg_to_lbs(100))
numbers = [3, 6, 4, 1]
print(find_max(numbers))
# print(converters.kg_to_lbs(70))
# print(converters.name)
