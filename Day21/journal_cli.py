"""
journal_cli.py

Command-line interface for the Daily Journal app.
Uses functions from journal_core.py.
"""

from journal_core import (
    add_entry_for_today,
    view_all_entries,
    view_entries_for_date,
)


def show_menu():
    print("\n=== Daily Journal ===")
    print("1) Add entry for today")
    print("2) View all entries")
    print("3) View entries for a specific date")
    print("4) Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_entry_for_today()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            target_date = input("Enter date (YYYY-MM-DD): ").strip()
            if target_date:
                view_entries_for_date(target_date)
            else:
                print("No date entered.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
