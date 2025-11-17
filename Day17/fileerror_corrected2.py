file_name = "notes.txt"

try:
    with open(file_name, "r") as f:
        content = f.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    create = input("Do you want to create it? (y/n): ").lower()
    if create == "y":
        with open(file_name, "w") as f:
            f.write("")  # start with an empty file
        print(f"Created empty file '{file_name}'.")
    else:
        print("Okay, not creating the file.")
