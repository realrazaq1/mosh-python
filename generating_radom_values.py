# python comes with standard library that contains several modules for common tasks such as sending emails, working with date and time, generating random values and passwords, etc
# where to find the standard library: search for "python 3 module index" on google. click the first link. there you will find all the modules built into python

import random

# .random() - returns random value between 0-1
# for i in range(3):
#     print(random.random())

# randint() - you can specify the range u want
names = ["raz", "kaz", "muazz", "taiwo"]
for i in range(3):
    print(random.randint(0, len(names) - 1))

# print random name
random_num = random.randint(0, len(names) - 1)
print(names[random_num])

# .choice => randomly pick an item from a list
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)