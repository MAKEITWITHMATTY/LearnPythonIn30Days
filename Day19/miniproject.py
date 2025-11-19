import random
import datetime
import math

def roll_dice():
    roll = random.randint(1, 6)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    power = math.pow(roll, 2)  # just for fun!

    return f"""
🎲 Dice Rolled!
Result: {roll}
Result squared (math.pow): {power}
Time: {timestamp}
"""

print(roll_dice())
