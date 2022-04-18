# we use logical operators in situations where we have multiple conditions
# e.g if applicant has high income AND good credit, applicant is eligible for loan

# and => both conditions have to be True
# or => at least one or both of the conditions should be True
# not => inverses a boolean value

has_high_income = True
has_good_credit = False

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

name = "Razaq"
if not name == "Razaq":
    print("Welcome regular user")
else:
    print("Welcome super user")