import random

print(random.random())          # 0.0 to 1.0
print(random.randint(1, 6))     # random number between 1–6
print(random.choice(["orc", "troll", "slime"]))  # random pick

weapons = ["Sword", "Axe", "Bow", "Dagger"]
print("You found a:", random.choice(weapons))
