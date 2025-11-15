# Day 14 – Tiny Dungeon (Week 2 Review)
# Uses concepts from Days 1–13: variables, input/print, operators, conditionals,
# loops, lists, tuples, sets, dictionaries, nested structures & traversal.

# ---------- World Setup (nested dictionaries/lists/sets/tuples) ----------
ROOMS = {
    "hall": {
        "desc": "A dim hall with cracked tiles. Exits: east, south.",
        "exits": {"east": "armory", "south": "library"},
        "item": "bandage"
    },
    "armory": {
        "desc": "Dusty racks. A simple shield leans on a wall. Exits: west.",
        "exits": {"west": "hall"},
        "item": "shield"
    },
    "library": {
        "desc": "Stacks of books. A faint growl below. Exits: north, down.",
        "exits": {"north": "hall", "down": "crypt"},
        "item": "tome"
    },
    "crypt": {
        "desc": "Cold air. The final guardian stirs. Exits: up.",
        "exits": {"up": "library"},
        "item": None
    },
}

# Attacks: list of dictionaries (Day 10 + 12)
ATTACKS = [
    {"name": "strike", "cost": 2, "tags": {"slash"}, "base": 4},
    {"name": "bash",   "cost": 3, "tags": {"blunt"}, "base": 6},
    {"name": "pierce", "cost": 2, "tags": {"pierce"}, "base": 5},
]

# Tuple config: fixed (Day 11: tuples)
HEAL_RANGE = (5, 5)   # fixed heal of 5 (min,max same); demonstrates tuple
GUARD_REDUCTION = (3,)  # tuple of one value, reduces incoming damage by 3

# Monsters: list of dictionaries; each has a weakness set (Day 11: sets)
MONSTERS = [
    {
        "name": "Ratling",
        "hp": 10,
        "attack": 3,
        "weakness": {"slash", "pierce"},
        "room": "hall",
        "alive": True
    },
    {
        "name": "Bone Knight",
        "hp": 18,
        "attack": 4,
        "weakness": {"blunt"},
        "room": "library",
        "alive": True
    },
    {
        "name": "Crypt Warden",
        "hp": 24,
        "attack": 5,
        "weakness": {"pierce", "blunt"},
        "room": "crypt",
        "alive": True
    }
]

# Player dictionary (Day 12)
player = {
    "hp": 20,
    "max_hp": 20,
    "stamina": 8,
    "max_stamina": 8,
    "location": "hall",
    "inventory": set(),  # Day 11: set avoids duplicates
    "guarding": False
}

# Battle log (Day 10 slicing later)
log = []

# ---------- Utility Functions (no imports yet – Week 2 only) ----------
def add_log(message):
    log.append(message)
    # keep log modest; demonstrate list slicing by trimming
    if len(log) > 50:
        del log[:10]  # remove the oldest 10 entries

def current_monster():
    """Return the living monster in the player's room, or None (Day 12 .get)"""
    for m in MONSTERS:
        if m.get("room") == player["location"] and m.get("alive"):
            return m
    return None

def show_room():
    room = ROOMS[player["location"]]
    print(f"\n📍 {player['location'].upper()}")
    print(room["desc"])
    if room["item"]:
        print(f"🪄 You see a {room['item']}. Type: take {room['item']}")
    # show exits using a for loop (Day 8)
    exits = ", ".join(room["exits"].keys())
    print(f"Exits: {exits}")
    m = current_monster()
    if m:
        print(f"👹 A {m['name']} is here! HP: {m['hp']}  Weak: {', '.join(sorted(m['weakness']))}")

def show_status():
    print(f"❤️ HP {player['hp']}/{player['max_hp']}   ⚡ STA {player['stamina']}/{player['max_stamina']}")
    print(f"🎒 Bag: {', '.join(sorted(player['inventory'])) if player['inventory'] else '(empty)'}")

def clamp(val, lo, hi):
    return lo if val < lo else hi if val > hi else val

def compute_damage(attack_dict, monster):
    # Base damage + weakness bonus via set intersection (Day 11)
    tags = attack_dict["tags"]
    base = attack_dict["base"]
    bonus = 2 if (tags & monster["weakness"]) else 0
    return base + bonus

def living_monsters_count():
    c = 0
    for m in MONSTERS:
        if m["alive"]:
            c += 1
    return c

# ---------- Game Commands ----------
def cmd_go(direction):
    room = ROOMS[player["location"]]
    if direction in room["exits"]:
        player["location"] = room["exits"][direction]
        add_log(f"Moved to {player['location']}.")
        show_room()
    else:
        print("🚪 You can’t go that way.")

def cmd_take(item_name):
    room = ROOMS[player["location"]]
    if room["item"] == item_name:
        player["inventory"].add(item_name)  # set stores unique
        room["item"] = None
        print(f"Picked up {item_name}.")
        add_log(f"Took {item_name}.")
    else:
        print("Nothing like that here.")

def cmd_attacks():
    print("\nAvailable attacks (name / cost / tags / base):")
    for a in ATTACKS:
        print(f" - {a['name']} / {a['cost']} / {','.join(sorted(a['tags']))} / {a['base']}")

def cmd_info():
    m = current_monster()
    if not m:
        print("No monster here.")
        return
    print(f"{m['name']} — HP {m['hp']} / ATK {m['attack']} / Weak: {', '.join(sorted(m['weakness']))}")

def cmd_log():
    # Show last 8 entries using slicing (Day 10)
    recent = log[-8:]
    print("\n--- Recent Log ---")
    for line in recent:
        print(line)
    print("------------------")

# ---------- Battle Actions ----------
def action_attack(parts):
    if len(parts) < 2:
        print("Usage: attack <strike|bash|pierce>")
        return
    m = current_monster()
    if not m:
        print("No monster to attack.")
        return

    name = parts[1]
    attack = None
    for a in ATTACKS:
        if a["name"] == name:
            attack = a
            break

    if not attack:
        print("Unknown attack. Try: strike, bash, pierce")
        return

    cost = attack["cost"]
    if player["stamina"] < cost:
        print("Too tired. Try 'guard' to reduce damage next hit or 'heal' to recover HP.")
        return

    dmg = compute_damage(attack, m)
    m["hp"] -= dmg
    player["stamina"] -= cost
    add_log(f"You used {name} for {dmg} damage.")

    if m["hp"] <= 0:
        m["alive"] = False
        add_log(f"Defeated {m['name']}!")
        print(f"🏆 {m['name']} defeated!")
        # small stamina bump on kill (operators Day 4)
        player["stamina"] = clamp(player["stamina"] + 2, 0, player["max_stamina"])
        return

    # Monster counterattacks (deterministic)
    incoming = m["attack"]
    if player["guarding"]:
        incoming -= GUARD_REDUCTION[0]
        incoming = max(0, incoming)
        player["guarding"] = False
        add_log("Your guard reduces damage!")

    player["hp"] -= incoming
    add_log(f"{m['name']} hits you for {incoming}.")

def action_heal():
    # Heals 5 HP; if you have 'bandage' or 'tome', heal more (demonstrates conditionals)
    base_heal = HEAL_RANGE[0]  # 5
    bonus = 0
    if "bandage" in player["inventory"]:
        bonus += 2
    if "tome" in player["inventory"]:
        bonus += 1
    amount = base_heal + bonus
    player["hp"] = clamp(player["hp"] + amount, 0, player["max_hp"])
    add_log(f"You heal {amount} HP.")

def action_guard():
    # Reduces next hit; if you have 'shield', also refund 1 stamina (chained conditions)
    player["guarding"] = True
    if "shield" in player["inventory"] and player["stamina"] < player["max_stamina"]:
        player["stamina"] += 1
        add_log("You brace behind the shield and regain 1 stamina.")
    else:
        add_log("You raise your guard.")

def action_bag():
    show_status()
    cmd_attacks()

# ---------- Win/Lose ----------
def check_win_or_lose():
    if player["hp"] <= 0:
        print("\n💀 You collapse. Game over.")
        return True
    if living_monsters_count() == 0 and player["location"] == "hall":
        print("\n🎉 You cleared the dungeon and returned to the hall. Victory!")
        return True
    return False

# ---------- Game Loop (Day 9 while + Day 8 for loops inside helpers) ----------
def main():
    print("=== Tiny Dungeon — Week 2 Review ===")
    print("Type 'help' for commands.")
    show_room()
    show_status()

    while True:
        if check_win_or_lose():
            break

        cmd = input("\n> ").strip().lower()  # Day 3 input + Day 2 string ops
        if not cmd:
            continue

        parts = cmd.split()
        verb = parts[0]

        if verb in ("quit", "exit"):
            print("Thanks for playing!")
            break

        elif verb == "help":
            print("""
Commands:
  go <dir>        - move (north/south/east/west/up/down)
  take <item>     - pick up an item in the room
  attack <name>   - strike | bash | pierce
  heal            - restore HP (more with items)
  guard           - reduce next hit (shield helps stamina)
  info            - show monster info (if present)
  bag             - show HP, stamina, inventory & attacks
  log             - recent battle messages
  look            - re-describe the room
  home            - return to the hall if all monsters are defeated (win)
  quit            - exit
            """)

        elif verb == "look":
            show_room()

        elif verb == "home":
            if living_monsters_count() == 0:
                player["location"] = "hall"
                show_room()
            else:
                print("Monsters still roam. Clear them first.")

        elif verb == "go" and len(parts) >= 2:
            direction = parts[1]
            cmd_go(direction)

        elif verb == "take" and len(parts) >= 2:
            item = parts[1]
            cmd_take(item)

        elif verb == "attack":
            action_attack(parts)

        elif verb == "heal":
            action_heal()

        elif verb == "guard":
            action_guard()

        elif verb == "bag":
            action_bag()

        elif verb == "info":
            cmd_info()

        elif verb == "log":
            cmd_log()

        else:
            print("I don't understand. Type 'help'.")

        # Passive stamina regen each turn (operator/conditional)
        if player["stamina"] < player["max_stamina"]:
            player["stamina"] += 1

        # Soft lose hint
        if player["hp"] <= 6 and "bandage" in player["inventory"]:
            add_log("Hint: Use 'heal' — your bandage boosts it!")

        # Show status summary after each command
        show_status()

if __name__ == "__main__":
    main()
