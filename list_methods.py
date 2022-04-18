# list methods are operations we can perform on a list
numbers = [5, 2, 1, 2, 2, 7, 4]

# add to the end of list
numbers.append(20)
print(numbers)

# insert at a particular index
numbers.insert(0, 10)
print(numbers)

# remove at item
numbers.remove(5)
print(numbers)

# remove all items
# numbers.clear()
# print(numbers)

# remove the last item
numbers.pop()
print(numbers)

# check if a value exist in the list
print(25 in numbers)
print(2 in numbers)

# count the occurrence of an item
print(numbers.count(2))

# None is object in python that represent the absence of a value

# sort
# print(numbers.sort())
numbers.sort()
print(numbers)

# reverse the order
numbers.reverse()
print(numbers)

# copy a list
numbers2 = numbers.copy()
numbers.append(11)
print(numbers)
print(numbers2)
