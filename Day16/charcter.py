def create_character(name, role="Adventurer", *, hp=100, mp=50):
    """
    Creates a simple character profile.

    Parameters:
        name (str): Character name.
        role (str, optional): Character class. Defaults to "Adventurer".
        hp (int, keyword-only): Health points.
        mp (int, keyword-only): Magic points.

    Returns:
        dict: A character dictionary.
    """
    return {
        "name": name,
        "role": role,
        "hp": hp,
        "mp": mp
    }

# Examples
print(create_character("Elyra"))
print(create_character("Thorne", role="Warrior", hp=150, mp=20))
