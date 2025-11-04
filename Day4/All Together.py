age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket (yes/no)? ").strip().lower() == "yes"
is_vip = input("Are you on the VIP list (yes/no)? ").strip().lower() == "yes"

# Rule: You can enter if you're 18+ AND have a ticket.
# VIPs may enter with a ticket even if under 18 (house rule example).
if (age >= 18 and has_ticket) or (is_vip and has_ticket):
    print("Welcome to the concert!")
elif has_ticket and age < 18 and not is_vip:
    print("Sorry, you must be 18 or older (VIPs excepted).")
elif not has_ticket:
    print("You need a valid ticket to enter.")
else:
    print("Sorry, entry requirements not met.")
