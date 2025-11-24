class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

hero = Player("Matty", 100)
villain = Player("DarkBot", 80)

print(hero.name)     # Matty
print(villain.health)  # 80
