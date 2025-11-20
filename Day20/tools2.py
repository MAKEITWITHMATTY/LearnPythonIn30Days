# tools.py
"""
A tiny module containing helper functions for games.
"""

def roll_dice(sides=6):
    """Return a random dice roll from 1 to `sides`."""
    import random
    return random.randint(1, sides)

def format_title(title):
    """Return a title wrapped with dashes for better display."""
    return f"\n--- {title} ---\n"

if __name__ == "__main__":
    print("Testing tools module...")
    print(format_title("Demo"))
    print("Roll:", roll_dice(6))
