file_name = "notes.txt"

try:
    with open(file_name, "r") as f:
        content = f.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
