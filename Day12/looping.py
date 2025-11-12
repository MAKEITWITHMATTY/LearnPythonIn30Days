person = {"name": "Alex", "job": "Engineer", "country": "UK"}

# Loop over just keys
for key in person:
    print(key, ":", person[key])

# Loop over both key and value
for key, value in person.items():
    print(f"{key} → {value}")
