import json

try:
    with open("settings.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {
        "volume": 70,
        "fullscreen": False,
        "player_name": "New Player"
    }
