# we use dictionaries to store information that comes in form of key/value pair

# each key should be unique

customer = {
    "name": "John Smith",
    "email": "jsmith@gmail.com",
    "age": 50,
    "is_verified": True
}

# update
customer["name"] = "Elon Musk"
# print(customer["name"])
print(customer.get("name"))
