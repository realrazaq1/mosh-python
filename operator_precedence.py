# Operator precedence: order of operation
# PEMDAS => (), **, *, /, +, -
# x = 10 + 3 * 2 # 16
# x = (10 + 3) * 2  # 26 => (), *
# x = 10 + 3 * 2 ** 2  # 22 => **, *,+
# x = (10 + 3) * 2 ** 2  # 52 => (), **, *,+
x = (2 + 3) * 10 - 3  # 47
print(x)
