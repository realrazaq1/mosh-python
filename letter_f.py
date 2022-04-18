# numbers = [6, 2, 6, 2, 2] # F
numbers = [2, 2, 2, 2, 6]  # L
# for num in numbers:
#     print("x" * num)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
