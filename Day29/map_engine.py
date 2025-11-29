from utils import direction_from_input

def get_current_region(world, player):
    return world["regions"][player.location["region"]]

def get_current_tile(world, player):
    region = get_current_region(world, player)
    x = player.location["x"]
    y = player.location["y"]
    return region["map"][y][x]

def describe_location(world, player):
    region = get_current_region(world, player)
    tile = get_current_tile(world, player)

    print("\n--- Location ---")
    print(f"Region: {region['name']} ({region['id']})")
    print(f"Position: x={player.location['x']}, y={player.location['y']}")
    print(f"Terrain: {tile['terrain']}")
    print(f"Danger level: {tile['danger_level']}")

    if tile.get("feature") == "village":
        print("A village is here. (Village entry on Day 30.)")

def is_tile_blocking(tile):
    # Hard-block key terrain types. Adjust this if your generator
    # uses additional water-like terrains (e.g. 'ocean', 'lake', etc.).
    if tile["terrain"] in ("mountain", "river", "water"):
        return True
    return False

def move_player_overworld(player, world, command):
    direction = direction_from_input(command)
    if direction is None:
        print("Unknown direction. Use n/s/e/w.")
        return

    current_region_id = player.location["region"]
    region = world["regions"][current_region_id]
    tile = get_current_tile(world, player)

    # 1. Check the tile's movement rules
    if not tile["directions"].get(direction, False):
        print("You can't go that way.")
        return

    # 2. Propose new coordinates inside the current region
    x, y = player.location["x"], player.location["y"]

    if direction == "north":
        y -= 1
    elif direction == "south":
        y += 1
    elif direction == "east":
        x += 1
    elif direction == "west":
        x -= 1

    size_y = len(region["map"])
    size_x = len(region["map"][0])

    target_region_id = current_region_id
    region_changed = False

    # 3. Handle region edge transitions
    if x < 0:
        exit_id = region.get("exits", {}).get("west")
        if exit_id:
            target_region_id = exit_id
            region = world["regions"][exit_id]
            size_y = len(region["map"])
            size_x = len(region["map"][0])
            x = size_x - 1  # rightmost column of new region
            region_changed = True
        else:
            print("The world ends in a sheer cliff. You cannot go further west.")
            return
    elif x >= size_x:
        exit_id = region.get("exits", {}).get("east")
        if exit_id:
            target_region_id = exit_id
            region = world["regions"][exit_id]
            size_y = len(region["map"])
            size_x = len(region["map"][0])
            x = 0  # leftmost column
            region_changed = True
        else:
            print("An impassable boundary stops your journey east.")
            return

    if y < 0:
        exit_id = region.get("exits", {}).get("north")
        if exit_id:
            target_region_id = exit_id
            region = world["regions"][exit_id]
            size_y = len(region["map"])
            size_x = len(region["map"][0])
            y = size_y - 1  # bottom row
            region_changed = True
        else:
            print("Snow-capped peaks block the way north.")
            return
    elif y >= size_y:
        exit_id = region.get("exits", {}).get("south")
        if exit_id:
            target_region_id = exit_id
            region = world["regions"][exit_id]
            size_y = len(region["map"])
            size_x = len(region["map"][0])
            y = 0  # top row
            region_changed = True
        else:
            print("A chasm or wasteland blocks the way south.")
            return

    # 4. At this point, (x, y) must be valid inside `region`.
    new_tile = region["map"][y][x]
    if is_tile_blocking(new_tile):
        print("That terrain is impassable.")
        return

    # 5. Commit new position & region
    player.location["region"] = target_region_id
    player.location["x"] = x
    player.location["y"] = y

    if region_changed:
        print(f"You travel {direction} into {region['name']}.")
    else:
        print(f"You move {direction}.")
