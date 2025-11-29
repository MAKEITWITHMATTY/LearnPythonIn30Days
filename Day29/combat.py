import random

def show_player_stats(player):
    print("\n--- Player ---")
    print(f"HP: {player.health}")
    print(f"MP: {player.magic}")
    print(f"Level: {player.level}")
    print(f"XP: {player.xp}")
    print(f"Gold: {player.gold}")

def combat(player, base_creature):
    creature = dict(base_creature)
    creature_hp = creature["health"]

    print(f"\n=== Combat: {creature['name']} ===")

    while creature_hp > 0 and player.health > 0:
        print(f"\nYour HP: {player.health}")
        print(f"{creature['name']} HP: {creature_hp}")

        action = input("(a)ttack or (r)un? ").lower().strip()

        if action == "a":
            dmg = random.randint(2, 6)
            creature_hp -= dmg
            print(f"You hit the {creature['name']} for {dmg} damage.")
        elif action == "r":
            print("You escape!")
            return
        else:
            print("You hesitate...")

        if creature_hp > 0:
            player.health -= creature["attack"]
            print(f"The {creature['name']} strikes you for {creature['attack']}!")

    if player.health <= 0:
        print("\nYou have died...")
        raise SystemExit

    print(f"\nYou defeated the {creature['name']}!")
    player.xp += creature.get("xp", 0)
    player.gold += creature.get("gold", 0)
