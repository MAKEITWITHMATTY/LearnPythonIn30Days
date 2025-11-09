correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered = input("Enter your password: ")

    if entered == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

if attempts == max_attempts:
    print("Too many attempts! Access denied.")
