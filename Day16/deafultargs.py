def welcome(name, level="beginner"):
    print(f"Welcome {name}, you are set to {level} mode!")

welcome("Matty")                # uses default: beginner
welcome("Matty", level="pro")   # overrides the default
