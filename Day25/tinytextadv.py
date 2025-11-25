rooms = {
    "start": {
        "desc": "You are in a quiet room.",
        "exits": {"north": "forest"}
    },
    "forest": {
        "desc": "You are in a dark forest.",
        "exits": {"south": "start"}
    }
}

def describe_room(name):
    data = rooms[name]
    print(data["desc"])
    print("Exits:", ", ".join(data["exits"].keys()))

def move(room, direction):
    exits = rooms[room]["exits"]
    if direction in exits:
        return exits[direction]
    else:
        print("You can't go that way.")
        return room

def main():
    room = "start"
    while True:
        describe_room(room)
        cmd = input("> ")
        room = move(room, cmd)

main()
