contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add / Update Contact")
    print("2. View Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Quit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email (optional): ").strip()

        contacts[name] = {
            "phone": phone,
            "email": email if email else "Not provided"
        }
        print(f"Saved contact for {name}.")

    elif choice == "2":
        name = input("Enter name to look up: ").strip()
        contact = contacts.get(name)
        if contact:
            print(f"\n{name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("No contact found with that name.")

    elif choice == "3":
        if not contacts:
            print("No contacts saved yet.")
        else:
            print("\nAll contacts:")
            for name, info in contacts.items():
                print(f"- {name}: {info['phone']} ({info['email']})")

    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        removed = contacts.pop(name, None)
        if removed:
            print(f"Deleted contact for {name}.")
        else:
            print("No contact found with that name.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
