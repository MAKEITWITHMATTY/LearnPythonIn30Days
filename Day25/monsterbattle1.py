import random

print("Battle Start!")
hp = 20
monster_hp = 15

while hp > 0 and monster_hp > 0:
    dmg = random.randint(1, 6)
    monster_hp -= dmg
    print("You hit the monster for", dmg)

    if monster_hp <= 0:
        break

    mdmg = random.randint(1, 4)
    hp -= mdmg
    print("The monster hits you for", mdmg)

print("You win!" if hp > 0 else "Monster wins!")
