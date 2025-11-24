class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} now has {self.health} HP.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals to {self.health} HP.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

hero = Player("Matty")

hero.take_damage(30)
hero.heal(10)
hero.add_item("Sword")
hero.add_item("Health Potion")

print(hero.inventory)
