# if statements are extremely important in programming. they allow us build programs that can make decisions based on some conditions

is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    pass
print("Enjoy your day")
# Exercise
price_of_house = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = price_of_house * 0.10
else:
    down_payment = price_of_house * 0.20
print(f'Down payment: ${down_payment}')

phone_number = input("Enter phone number: ")
if phone_number == '08130069772':
    print("You are RAZAQ 😎")
else:
    print("You are not Razaq 😡")
