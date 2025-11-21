"""
journal_core.py

Core logic for the Daily Journal app:
- getting today's date
- adding entries
- viewing entries
"""

from datetime import date

JOURNAL_FILE = "journal.txt"


def get_today_str():
    """Return today's date as a YYYY-MM-DD string."""
    return date.today().isoformat()


def add_entry_for_today():
    """Let the user type a journal entry for today and save it."""
    today = get_today_str()
    print(f"\nWriting entry for {today}.")
    print("Type your entry. Press Enter on an empty line to finish.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("No text entered. Entry cancelled.")
        return

    entry_text = "\n".join(lines)

    try:
        with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
            f.write(f"=== {today} ===\n")
            f.write(entry_text + "\n\n")
        print("Entry saved!")
    except OSError as e:
        print("Something went wrong while saving your entry:")
        print(e)


def view_all_entries():
    """Read and print all journal entries."""
    print("\n=== All Journal Entries ===\n")

    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("No journal file found yet. Write your first entry!")
        return
    except OSError as e:
        print("Could not read the journal file:")
        print(e)
        return

    if not content.strip():
        print("Journal is empty for now.")
    else:
        print(content)


def view_entries_for_date(target_date):
    """Show entries that match a specific date (YYYY-MM-DD)."""
    header = f"=== {target_date} ==="

    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No journal file found yet. Write your first entry!")
        return
    except OSError as e:
        print("Could not read the journal file:")
        print(e)
        return

    matching_entries = []
    current_entry_lines = []
    in_matching_entry = False

    for line in lines:
        if line.startswith("===") and "===" in line:
            # starting a new entry block
            if in_matching_entry and current_entry_lines:
                matching_entries.append("".join(current_entry_lines))
            current_entry_lines = []

            if line.strip() == header:
                in_matching_entry = True
                current_entry_lines.append(line)
            else:
                in_matching_entry = False
        else:
            if in_matching_entry:
                current_entry_lines.append(line)

    # catch last entry
    if in_matching_entry and current_entry_lines:
        matching_entries.append("".join(current_entry_lines))

    if not matching_entries:
        print(f"No entries found for {target_date}.")
    else:
        print(f"\n=== Entries for {target_date} ===\n")
        for entry in matching_entries:
            print(entry)
            print("-" * 40)
