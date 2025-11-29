# generators/village_generator.py
import json
import os
import random

from npc_generator import create_npc

VILLAGE_NAMES = [
    "Stonebrook", "Riverford", "Ashgate", "Frostwatch",
    "Moonhollow", "Ironhelm", "Windrest"
]

BUILDING_TYPES = ["house", "shop", "inn", "farm", "empty", "empty"]

def movement_for_village_tile(tile_type):
    """
    Movement rules inside a village:
    - 'path' tiles: walkable in all directions
    - building tiles (house/shop/inn/farm): blocked in all directions
    - 'empty' can be walkable (like open ground)
    """
    directions = {
        "north": False,
        "south": False,
        "east": False,
        "west": False
    }

    if tile_type in ("path", "empty"):
        for key in directions:
            directions[key] = True

    return directions

def generate_village_map(width=5, height=5):
    """
    Create a simple village layout:
    - central 'path' down the middle
    - random buildings on either side
    - each tile includes movement directions (N/S/E/W only)
    """
    village_map = []
    for y in range(height):
        row = []
        for x in range(width):
            if x == width // 2:
                tile_type = "path"
            else:
                tile_type = random.choice(BUILDING_TYPES)

            tile = {
                "type": tile_type,
                "directions": movement_for_village_tile(tile_type)
            }
            row.append(tile)
        village_map.append(row)
    return village_map

def build_village_entry(village_info):
    """
    Take a village position from world.json and build a full village entry.
    village_info looks like:
      { "id": "...", "name": None, "region": "green_valley", "x": 3, "y": 7 }
    """
    name = random.choice(VILLAGE_NAMES)
    npc_count = random.randint(2, 5)

    npcs = [create_npc() for _ in range(npc_count)]

    return {
        "id": village_info["id"],
        "name": name,
        "region": village_info["region"],
        "world_x": village_info["x"],
        "world_y": village_info["y"],
        "map": generate_village_map(),
        "npcs": npcs
    }

def load_world(path="../data/world.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_villages(villages, path="../data/villages.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(villages, f, indent=2)

if __name__ == "__main__":
    world = load_world()
    villages = []

    for village_info in world["villages"]:
        v = build_village_entry(village_info)
        villages.append(v)

    save_villages(villages)
    print(f"Generated {len(villages)} villages and saved to data/villages.json")
