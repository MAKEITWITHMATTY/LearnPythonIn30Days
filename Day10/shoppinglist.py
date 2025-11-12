# Shopping List Manager

shopping_list = []

while True:
    print("\nYour list:", shopping_list)
    print("Options: add, remove, quit")
    choice = input("What would you like to do? ").lower()

    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added!")

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif choice == "quit":
        print("Final list:", shopping_list)
        break

    else:
        print("Invalid option.")
