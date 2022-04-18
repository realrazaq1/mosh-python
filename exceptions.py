# error handling
# exit code 0: means our program terminated successfully
# exit code 1: program crashed
# as programmer u should anticipate this kind of situations and handle it by printing proper error message
# we use try/except to handle errors, just like try/catch in javascript
# an exception is a kind of error that crashes the program

try:
    age = int(input("Age:"))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0!!")
except ValueError:
    print("Invalid value")
