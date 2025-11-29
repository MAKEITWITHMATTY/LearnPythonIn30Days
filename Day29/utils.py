def direction_from_input(command):
    mapping = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west"
    }
    return mapping.get(command.lower())
