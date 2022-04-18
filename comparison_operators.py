# Logical Operators
# >, >=, <, <=, ==, !=
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Exercise
name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 chars long")
elif len(name) > 50:
    print("Name cannot be more than 50 chars")
else:
    print("Name looks good!")
