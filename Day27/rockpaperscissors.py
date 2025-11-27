import random  # Day 19 - modules

VALID_CHOICES = ["rock", "paper", "scissors"]


def get_player_choice():
    """Ask the player for a choice and return it in lowercase."""
    while True:
        choice = input("Choose Rock, Paper or Scissors: ").strip().lower()

        # Day 17 – error handling mindset
        if choice not in VALID_CHOICES:
            print("Invalid choice! Try again.")
            continue
        return choice


def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(VALID_CHOICES)


def determine_winner(player, computer):
    """Return 'player', 'computer', or 'draw' depending on who wins."""
    if player == computer:
        return "draw"

    # Day 5–6: conditionals + logical operators
    if (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "player"
    else:
        return "computer"


def play_round():
    """Play one round of RPS and return the result."""
    player = get_player_choice()       # Day 3 & 7 input handling
    computer = get_computer_choice()   # Day 19 modules + randomness

    print(f"\nYou chose:     {player}")
    print(f"Computer chose:{computer}\n")

    outcome = determine_winner(player, computer)

    if outcome == "draw":
        print("It's a draw!")
    elif outcome == "player":
        print("You win! 🎉")
    else:
        print("Computer wins!")

    return outcome


def main():
    """Main game loop."""
    print("=== Rock Paper Scissors ===")
    print("Type Ctrl+C or 'quit' at any time to stop.\n")

    scores = {"player": 0, "computer": 0, "draw": 0}

    while True:     # Day 9 while loops
        result = play_round()
        scores[result] += 1

        print("\nScoreboard:")
        print(f"You: {scores['player']} | Computer: {scores['computer']} | Draws: {scores['draw']}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
