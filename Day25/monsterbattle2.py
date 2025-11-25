import random

def roll_damage(min_dmg, max_dmg):
    return random.randint(min_dmg, max_dmg)

def player_turn(monster_hp):
    dmg = roll_damage(2, 6)
    monster_hp -= dmg
    print(f"You deal {dmg} damage!")
    return monster_hp

def monster_turn(player_hp):
    dmg = roll_damage(1, 4)
    player_hp -= dmg
    print(f"The monster hits you for {dmg}!")
    return player_hp

def print_status(player_hp, monster_hp):
    print(f"Player HP: {player_hp} | Monster HP: {monster_hp}\n")

def main():
    player_hp = 20
    monster_hp = 15
    print("=== Tiny Monster Battle ===")

    while player_hp > 0 and monster_hp > 0:
        monster_hp = player_turn(monster_hp)
        print_status(player_hp, monster_hp)

        if monster_hp <= 0:
            break
        
        player_hp = monster_turn(player_hp)
        print_status(player_hp, monster_hp)

    print("🎉 You win!" if player_hp > 0 else "💀 The monster defeated you!")

main()
