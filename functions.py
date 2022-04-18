# a function is a container for a few lines of code that performs a specific task
# def <function-name>():
#      ...block of code
# parameters are the placeholders/variables
# arguments are the values we supply to the function

# positional arguments: means the position or order of these arguments matters

# we also have keyword arguments. the position does not matter

# for the most part, use positional args. But if you are dealing with functions that takes in numerical values as arguments try to use keyword arguments to improve the readability of your code

# keyword args should always come after positional args

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


# greet_user(last_name="Musk", first_name="Elon")
greet_user("Elon", "Musk")
