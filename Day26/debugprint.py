def total_price(prices):
    total = 0
    for p in prices:
        print("DEBUG: p =", p, "| type:", type(p))
        total += float(p)
    return total

items = ["4.99", "2.50", "10.00"]
print(total_price(items))
