person = {
    "name": "Alex",
    "job": "Engineer",
    "country": "UK"
}

# Using the dict() constructor
settings = dict(theme="dark", autosave=True)

# Creating an empty dictionary
data = {}

# Keys must be unique; duplicates overwrite
demo = {"name": "Alex", "name": "Sam"}

print("Person:", person)
print("Settings:", settings)
print("Empty:", data)
print("Duplicate key example:", demo)
