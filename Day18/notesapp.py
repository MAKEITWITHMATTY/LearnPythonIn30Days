NOTES_FILE = "notes.txt"

def load_notes():
    """Read all notes from the file."""
    try:
        with open(NOTES_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []  # Create a new empty notes file later

def save_notes(notes):
    """Write the entire list of notes back to the file."""
    with open(NOTES_FILE, "w") as f:
        for note in notes:
            f.write(note + "\n")

def show_notes(notes):
    if not notes:
        print("\nNo notes yet.\n")
    else:
        print("\nYour Notes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
        print()

def main():
    notes = load_notes()

    while True:
        print("=== Simple Notes App ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_notes(notes)

        elif choice == "2":
            new_note = input("Type your note: ")
            notes.append(new_note)
            save_notes(notes)
            print("Note added!\n")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")

main()
