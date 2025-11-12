person = {"name": "Alex", "age": 30, "city": "London"}

# Delete by key
del person["city"]

# Delete and return a value
age = person.pop("age")
print("Removed age:", age)

# Safe delete (no error if key not found)
person.pop("email", "No email found")

# Clear everything
person.clear()
print("After clear:", person)
