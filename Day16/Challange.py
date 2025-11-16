def create_character(
    name,
    role="Adventurer",
    weapon="Wooden Sword",
    is_npc=False,
    *,
    faction="Neutral"
):
    """
    Creates an RPG character profile with optional defaults and
    keyword-only arguments.

    Parameters:
        name (str): The character's name.
        role (str, optional): Character class or job.
                             Defaults to "Adventurer".
        weapon (str, optional): Starting weapon.
                                Defaults to "Wooden Sword".
        is_npc (bool, optional): True if this character is a non-player
                                 character. Defaults to False.
        faction (str, keyword-only): The group, clan, or alignment the
                                     character belongs to.

    Returns:
        str: A nicely formatted, multi-line character summary.
    """

    return f"""
Character Profile
-----------------
Name:    {name}
Role:    {role}
Faction: {faction}
NPC?:    {"Yes" if is_npc else "No"}
Weapon:  {weapon}
"""

print(create_character("Elyra"))
print(create_character(
    "Thorne",
    role="Warrior",
    weapon="Battle Axe",
    is_npc=True,
    faction="Iron Legion"
))
