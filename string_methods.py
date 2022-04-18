course = "Python for Beginners"
# length of a string => len(). it's a general purpose function
print(len(course))
# phone_number = input("Enter phone number: ")
# print(len(phone_number))
# print(len([1, 2, 3, 4, 5]))

# upper case => .upper()
print(course.upper())
# lower case => .lower()
print(course.lower())
# title case => .title()
print(course.title())
# .find() => find a character or sequence of character in a string. returns the index of the first occurence. Case sensitive
print(course.find("P"))
print(course.find("for"))  # "for" begins at index 7
print(course.find('o'))
print(course.find("For"))  # returns -1 if the word or char does not exist

# .replace(old_string, new_string) => replace words/character
print(course.replace('Beginners', 'Absolute Beginner'))

# in operator => check if a value exist in something. Returns True or False
print("Python" in course)
print("0813" in "08130069772")
exts = ["0703", "0706", "0803", "0806", "0810"]
print("0813" in exts)
