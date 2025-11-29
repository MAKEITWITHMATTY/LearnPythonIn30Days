from player import Player
from world_data import load_world, load_villages, load_creatures
from map_engine import describe_location, move_player_overworld
from creatures import maybe_trigger_encounter
from combat import show_player_stats, combat

def start_game():
    world = load_world()
    villages = load_villages()
    creatures = load_creatures()

    player = Player()

    print("=== RetroRealm ===")
    print("World loaded successfully.")
    print(f"Starting region: {player.location['region']}")

    main_loop(player, world, villages, creatures)

def main_loop(player, world, villages, creatures):
    while True:
        describe_location(world, player)

        print("\nCommands: n/s/e/w, stats, q")
        cmd = input("> ").strip().lower()

        if cmd in ("q", "quit"):
            print("Thanks for playing!")
            break

        if cmd == "stats":
            show_player_stats(player)
            continue

        if cmd in ("n", "s", "e", "w"):
            move_player_overworld(player, world, cmd)
            maybe_trigger_encounter(world, creatures, player, combat)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    start_game()
