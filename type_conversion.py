# int() => convert something to integer
# float() => convert something to float
# bool() => convert something to boolean
# type() => returns the data type of a value
# the input() function always returns a string. if u are expecting a numerical value convert it to a int() or float()

# name = input("What's your name: ")
# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(f"Hey {name}, you are {age} years old")

# Weight Converter
weight_lbs = int(input("Weight (lbs): "))
weight_kg = weight_lbs * 0.45
print(weight_kg)