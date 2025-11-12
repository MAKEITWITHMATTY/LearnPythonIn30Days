# Dictionary inside a Dictionary
users = {
    "matty": {
        "name": "Matty",
        "role": "admin",
        "likes_python": True
    },
    "alex": {
        "name": "Alex",
        "role": "editor",
        "likes_python": False
    }
}

print(users["matty"]["role"])

# List inside a Dictionary
playlist = {
    "name": "Coding Tunes",
    "songs": ["Track 1", "Track 2", "Track 3"]
}

print("Playlist name:", playlist["name"])
print("Songs:", playlist["songs"])

# Dictionaries inside a List
products = [
    {"name": "Soldering Iron", "price": 25.0},
    {"name": "Breadboard", "price": 5.0}
]

for product in products:
    print(f"{product['name']} - £{product['price']}")
