# generators/npc_generator.py
import random

HUMAN_NAMES = ["Torren", "Elda", "Marin", "Garron", "Lysa"]
ELF_NAMES   = ["Aeloria", "Thalan", "Seren", "Lirael"]
DWARF_NAMES = ["Borin", "Durik", "Thrug", "Helga"]

RACES = ["human", "elf", "dwarf"]

ROLES = {
    "shopkeeper": {
        "dialogue": [
            "Take a look at my wares.",
            "Gold talks, friend."
        ],
        "base_stats": {"health": 15, "magic": 5, "level": 1}
    },
    "farmer": {
        "dialogue": [
            "The land’s been harsh this year.",
            "Seen any wolves near the valley?"
        ],
        "base_stats": {"health": 18, "magic": 0, "level": 1}
    },
    "guard": {
        "dialogue": [
            "Stay out of trouble.",
            "Bandits have been bold lately."
        ],
        "base_stats": {"health": 25, "magic": 0, "level": 2}
    },
    "healer": {
        "dialogue": [
            "May your wounds mend swiftly.",
            "The forest whispers warnings..."
        ],
        "base_stats": {"health": 20, "magic": 15, "level": 2}
    }
}

def random_name_for_race(race):
    if race == "human":
        return random.choice(HUMAN_NAMES)
    if race == "elf":
        return random.choice(ELF_NAMES)
    if race == "dwarf":
        return random.choice(DWARF_NAMES)
    return "Nameless"

def create_npc(race=None, role=None):
    """
    Generate an NPC dict with race, role, dialogue, inventory, and stats.
    """
    if race is None:
        race = random.choice(RACES)
    if role is None:
        role = random.choice(list(ROLES.keys()))

    template = ROLES[role]
    base_stats = template["base_stats"]

    npc = {
        "name": random_name_for_race(race),
        "race": race,
        "role": role,
        "dialogue": template["dialogue"],
        "inventory": [],
        "stats": {
            "health": base_stats["health"],
            "magic": base_stats["magic"],
            "level": base_stats["level"]
        }
    }
    return npc

if __name__ == "__main__":
    # quick test
    for _ in range(3):
        print(create_npc())
