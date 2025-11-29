# generators/creature_generator.py
import json
import os

CREATURES = {
    "green_valley": [
        {"id": "wolf",   "name": "Wolf",         "health": 8,  "attack": 2, "xp": 5,  "min_danger": 1},
        {"id": "goblin", "name": "Goblin",       "health": 10, "attack": 3, "xp": 8,  "min_danger": 2},
    ],
    "ashen_wastes": [
        {"id": "scarab", "name": "Fire Scarab",  "health": 9,  "attack": 3, "xp": 7,  "min_danger": 1},
        {"id": "imp",    "name": "Ash Imp",      "health": 14, "attack": 4, "xp": 12, "min_danger": 2},
        {"id": "troll",  "name": "Lava Troll",   "health": 20, "attack": 5, "xp": 20, "min_danger": 3},
    ],
    "frostlands": [
        {"id": "wolf_ice", "name": "Ice Wolf",   "health": 10, "attack": 3, "xp": 9,  "min_danger": 1},
        {"id": "yeti",     "name": "Young Yeti", "health": 18, "attack": 4, "xp": 16, "min_danger": 2},
    ],
    # You can expand moonshadow / ironlands later
}

def save_creatures(path="../data/creatures.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(CREATURES, f, indent=2)

if __name__ == "__main__":
    save_creatures()
    print("Creature data saved to data/creatures.json")
