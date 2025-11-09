import getpass
import time

correct_password = "python123"
attempts = 0
max_attempts = 3
lockout_time = 10  # seconds

def safe_getpass(prompt="Enter your password: "):
    try:
        return getpass.getpass(prompt)
    except (getpass.GetPassWarning, Exception):
        # Fallback if hidden input isn’t possible
        print("Warning: Password may be visible.")
        return input(prompt)

while True:
    if attempts >= max_attempts:
        print(f"\nToo many failed attempts! Locked out for {lockout_time} seconds...")
        time.sleep(lockout_time)
        attempts = 0
        print("\nYou can try again.\n")

    entered = safe_getpass("Enter your password: ")

    if entered == correct_password:
        print("Access granted! Welcome back.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. Attempts left: {max_attempts - attempts}")
