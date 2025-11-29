import random
from map_engine import get_current_tile

def choose_creature_for_tile(world, creatures, player):
    region_id = player.location["region"]
    region_creatures = creatures.get(region_id, [])

    tile = get_current_tile(world, player)
    danger = tile["danger_level"]

    if danger <= 0:
        return None

    valid = [
        c for c in region_creatures
        if c.get("min_danger", 0) <= danger
    ]

    return random.choice(valid) if valid else None

def maybe_trigger_encounter(world, creatures, player, combat_func):
    tile = get_current_tile(world, player)
    danger = tile["danger_level"]

    if danger <= 0:
        return

    if random.randint(1, 10) > danger:
        return

    creature = choose_creature_for_tile(world, creatures, player)
    if creature:
        print(f"\nA wild {creature['name']} appears!")
        combat_func(player, creature)
