import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_world():
    return load_json("data/world.json")

def load_villages():
    return load_json("data/villages.json")

def load_creatures():
    return load_json("data/creatures.json")
