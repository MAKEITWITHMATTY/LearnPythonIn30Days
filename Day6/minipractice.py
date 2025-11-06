item = input("Enter item (chips/drink): ")
money = float(input("Insert money: "))

if item == "chips" and money >= 1.5:
    print("Enjoy your chips!")
elif item == "drink" and money >= 2.0:
    print("Here’s your drink!")
elif money < 1.5:
    print("Not enough money.")
else:
    print("Invalid item.")
