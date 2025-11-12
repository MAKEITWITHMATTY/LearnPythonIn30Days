person = {"name": "Alex", "job": "Engineer", "country": "UK"}

# Access directly
print(person["name"])   # Output: Alex

# Access using .get()
print(person.get("email", "Not provided"))
