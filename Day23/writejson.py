import json

settings = {
    "volume": 100,
    "fullscreen": False,
    "player_name": "Nova"
}

with open("wsettings.json", "w") as file:
    json.dump(settings, file, indent=4)
