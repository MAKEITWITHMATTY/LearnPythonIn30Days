def stats(numbers):
    return min(numbers), max(numbers)

low, high = stats([4, 9, 1, 7])
print(low, high)  # 1 9
