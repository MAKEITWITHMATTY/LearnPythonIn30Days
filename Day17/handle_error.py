def get_int(prompt):
    """Ask the user for an integer, keep asking until they give a valid one."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
            return value
        except ValueError:
            print("Please enter a whole number (no letters or symbols).")


age = get_int("Enter your age: ")
print("Next year you’ll be", age + 1)
