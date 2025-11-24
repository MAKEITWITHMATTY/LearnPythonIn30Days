import json

with open("rsettings.json", "r") as file:
    data = json.load(file)

data["volume"] = 50
data["fullscreen"] = True

with open("rsettings.json", "w") as file:
    json.dump(data, file, indent=4)
