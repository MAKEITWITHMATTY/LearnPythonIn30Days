prices = {"pedal": 40, "kit": 12, "resistors": 5}

with_tax = {item: price * 1.2 for item, price in prices.items()}

print(prices)
print(with_tax)
