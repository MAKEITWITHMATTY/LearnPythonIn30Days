class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, amount):
        self.score += amount
        print(f"{self.name}'s score is now {self.score}")

    def reset_score(self):
        self.score = 0
        print(f"{self.name}'s score has been reset.")

p1 = Player("Alice")
p2 = Player("Bob")

p1.add_score(10)   # Alice's score is now 10
p2.add_score(5)    # Bob's score is now 5

p1.reset_score()   # Alice's score has been reset.
