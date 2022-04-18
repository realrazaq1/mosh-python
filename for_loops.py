# we use for loops to iterate over items of a collection such as a string
names = ["Elon", "Mark", "Jack", "Bill"]  # list
# for item in "Python":
#     print(item)

# for item in names:
#     print(item)

# 0 - 9
# for item in range(10):
#     print(item)

# step
# for item in range(5, 10, 2):
#     print(item)

# total cost of items
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'Total: ${total}')
