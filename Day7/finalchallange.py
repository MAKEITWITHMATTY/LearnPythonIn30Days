# Learn Python in 30 Days — Day 7: Review Challenge
# Smart Tip Calculator
# Practice: input, variables, math, logic, and formatted output

print("Welcome to the Smart Tip Calculator!\n")

# Step 1 – Get inputs
bill = float(input("Enter total bill amount: £"))
service = input("How was the service? (good/average/poor): ").lower()
people = int(input("How many people to split the bill? "))

# Step 2 – Validate inputs
if bill > 0 and people > 0:
    # Step 3 – Determine tip percentage
    if service == "good":
        tip_percent = 0.20
    elif service == "average":
        tip_percent = 0.15
    elif service == "poor":
        tip_percent = 0.10
    else:
        tip_percent = 0.12  # default tip if unknown input

    # Step 4 – Calculate totals
    tip_amount = bill * tip_percent
    total = bill + tip_amount
    per_person = total / people

    # Step 5 – Display results
    print("\n--- Bill Summary ---")
    print(f"Service quality: {service}")
    print(f"Tip amount: £{tip_amount:.2f}")
    print(f"Total with tip: £{total:.2f}")
    print(f"Each person pays: £{per_person:.2f}")

else:
    print("\nError: Bill and number of people must be greater than zero.")
