groceries = ["milk", "bread"]
groceries.append("eggs")       # Add item to the end
print(groceries)

# Add one item
groceries.append("butter")
# Add multiple items
groceries.extend(["cheese", "apples"])
# Insert at a specific position
groceries.insert(1, "coffee")  # index 1, before 'bread'
print(groceries)


groceries.remove("bread")      # remove a specific item
print(groceries)

del groceries[0]               # delete by index (0 = first)
print(groceries)

popped = groceries.pop()       # removes and returns the last item
print("Removed:", popped)
print(groceries)

#clear the list
groceries.clear()
print(groceries)  # []
