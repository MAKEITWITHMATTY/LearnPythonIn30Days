numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # first three items
print(numbers[-2:])   # last two items

#You can even use a step value to skip through items:
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[::2])   # every second item → [10, 30, 50, 70]
print(numbers[1::2])  # every second item starting from index 1 → [20, 40, 60]

#Negative slicing is powerful too.
print(numbers[::-1])  # reverses the list!
