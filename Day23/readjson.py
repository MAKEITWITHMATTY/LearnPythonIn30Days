import json

with open("rsettings.json", "r") as file:
    data = json.load(file)

print(data)
