# use triple quotes for multi-line string
message = '''
Hi Razaq,
Here's our first email to you.
Thank you,
The support team
'''
# print(message)
course = "Python for Beginners"
print(course)
# use [] to get a character at a given index
print(course[0])
# use negative index to get characters at the end, [-1] last character, [-2] second character from the end, etc
print(course[-1], course[-2])
# extract characters [0:4] => 0 to 4 excluding 4
print(course[0:4])
# extract phone number prefix
# phone_number = input("Enter phone number: ")
# print(phone_number[0:4])

print(course[0:])  # index 0 to the end including the end
print(course[1:])  # index 1 to the end including the end
print(course[:5])  # index 0 to 5 excluding 5
# index 0 to the end. 0 will be assumed as the start index and the length of the string as the end index. We can use this syntax to copy a string
print(course[:])
name = "Jennifer"
print(name[1:-1])
print(name[1:])