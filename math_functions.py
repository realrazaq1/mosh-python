
# in python we have a handful of builtin functions for performing math operations. if u want to write a program that involves complex mathematical calculations, you need to import the math module

# a module in python is a separate file with some reusable code. we use modules to organize our code into different files

# search google for "python 3 math module" for the documentation

import math
# round()
x = 2.5
print(round(x))
# abs() => returns the +ve representation of a value
print(abs(-2.9))
# ceil() => rounds a number up. doesn't care about the decimal point
x = 2.1
print(math.ceil(x))
# floor() => rounds a number down. doesn't care about the decimal point
x = 2.9
print(math.floor(x))