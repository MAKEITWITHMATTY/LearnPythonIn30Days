# generators/world_generator.py
import json
import os
import random

TERRAINS = ["grass", "forest", "water", "mountain"]

REGIONS = {
    "green_valley": {
        "name": "Green Valley",
        "exits": {
            "north": "frostlands",
            "south": "ashen_wastes",
            "east": "moonshadow",
            "west": None
        }
    },
    "ashen_wastes": {
        "name": "Ashen Wastes",
        "exits": {"north": None, "south": None, "east": None, "west": "green_valley"}
    },
    "frostlands": {
        "name": "Frostlands",
        "exits": {"north": None, "south": "green_valley", "east": None, "west": None}
    },
    "moonshadow": {
        "name": "Moonshadow Woods",
        "exits": {"north": None, "south": None, "east": None, "west": "green_valley"}
    },
    "ironlands": {
        "name": "Ironlands",
        "exits": {"north": None, "south": None, "east": None, "west": None}
    }
}

def movement_for_terrain(terrain):
    """
    Return a directions dict for this terrain.
    Movement is restricted to north/south/east/west only.
    """
    # Start with all directions blocked
    directions = {
        "north": False,
        "south": False,
        "east": False,
        "west": False
    }

    # Grass and forest are walkable in all 4 directions
    if terrain in ("grass", "forest"):
        for key in directions:
            directions[key] = True

    # Water and mountains are fully blocked (impassable)
    # You can relax this later if you add boats, climbing, etc.

    return directions

def generate_tile():
    """Create a single world tile with terrain, feature, danger level, and movement rules."""
    terrain = random.choice(TERRAINS)

    # Forests & mountains a bit more dangerous
    if terrain in ("forest", "mountain"):
        danger = random.randint(1, 3)
    else:
        danger = random.randint(0, 2)

    return {
        "terrain": terrain,
        "feature": None,      # "village", "dungeon" etc (we only use "village" for now)
        "danger_level": danger,
        "directions": movement_for_terrain(terrain)
    }

def generate_map(size=10):
    """Generate a size×size map of tiles."""
    return [[generate_tile() for _ in range(size)] for _ in range(size)]

def place_villages(region_id, region_data, count=2):
    """
    Randomly place 'count' villages on a region map.
    Return a list of village entries {id, name, region, x, y}.
    """
    size = len(region_data["map"])
    villages = []

    for i in range(count):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)

        tile = region_data["map"][y][x]
        tile["feature"] = "village"

        village_id = f"{region_id}_village_{i}"
        villages.append({
            "id": village_id,
            "name": None,   # filled by village generator later
            "region": region_id,
            "x": x,
            "y": y
        })

    return villages

def build_world():
    """
    Build all regions with maps and village positions.
    Returns a dict ready to be saved as JSON.
    """
    world = {"regions": {}, "villages": []}

    for region_id, data in REGIONS.items():
        region_map = generate_map()
        region_entry = {
            "id": region_id,
            "name": data["name"],
            "map": region_map,
            "exits": data["exits"]
        }

        world["regions"][region_id] = region_entry

        # Place 1–2 villages
        village_count = random.randint(1, 2)
        villages = place_villages(region_id, region_entry, count=village_count)
        world["villages"].extend(villages)

    return world

def save_world(world, path="../data/world.json"):
    """Save the world dict as pretty-printed JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(world, f, indent=2)

if __name__ == "__main__":
    random.seed()  # or a fixed seed if you want reproducible worlds
    world_data = build_world()
    save_world(world_data)
    print("World generated and saved to data/world.json")
