class Player:
    def __init__(self):
        self.name = "Hero"

        self.health = 30
        self.magic = 15
        self.gold = 10
        self.xp = 0
        self.level = 1

        self.inventory = []
        self.owned_properties = {
            "houses": [],
            "shops": []
        }

        self.location = {
            "region": "green_valley",
            "x": 0,
            "y": 0
        }
