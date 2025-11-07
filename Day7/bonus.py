# Learn Python in 30 Days — Day 7: Bonus Challenge
# Smart Tip Calculator (Expanded)

print("Welcome to the Smart Tip Calculator!\n")

# Step 1 – Get currency symbol
currency = input("Choose your currency symbol (£, $, €): ").strip()
if currency not in ["£", "$", "€"]:
    print("Unknown symbol — defaulting to £.")
    currency = "£"

# Step 2 – Get inputs safely
try:
    bill = float(input(f"Enter total bill amount ({currency}): "))
    people = int(input("How many people to split the bill? "))
    service = input("How was the service? (good/average/poor): ").lower()

    # Step 3 – Validate input
    if bill <= 0 or people <= 0:
        print("\nError: Bill and number of people must be greater than zero.")
    else:
        # Step 4 – Determine tip percentage
        if service == "good":
            tip_percent = 0.20
        elif service == "average":
            tip_percent = 0.15
        elif service == "poor":
            tip_percent = 0.10
        else:
            tip_percent = 0.12  # default tip

        # Step 5 – Calculations
        tip_amount = bill * tip_percent
        total = bill + tip_amount
        per_person = total / people

        # Step 6 – Display results (formatted)
        print("\n--- Bill Summary ---")
        print(f"Service quality: {service}")
        print(f"Tip amount: {currency}{tip_amount:.2f}")
        print(f"Total with tip: {currency}{total:.2f}")
        print(f"Each person pays: {currency}{per_person:.2f}")

except ValueError:
    print("\nError: Please enter valid numeric values for the bill and number of people.")
