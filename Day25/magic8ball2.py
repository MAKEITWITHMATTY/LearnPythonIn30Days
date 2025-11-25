import random

def get_question():
    return input("Ask the Magic 8-Ball a question: ")

def get_random_answer():
    answers = [
        "Yes!",
        "No!",
        "Ask again later...",
        "It is certain.",
        "Very doubtful.",
        "Absolutely!",
        "Not today."
    ]
    return random.choice(answers)

def print_answer(answer):
    print("\n✨ The Magic 8-Ball says…")
    print("👉", answer)

def main():
    question = get_question()
    answer = get_random_answer()
    print_answer(answer)

main()
