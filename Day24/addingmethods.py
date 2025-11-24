class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Now at {self.health} HP.")

hero = Player("Matty", 100)
hero.take_damage(25)
# Matty took 25 damage! Now at 75 HP.
