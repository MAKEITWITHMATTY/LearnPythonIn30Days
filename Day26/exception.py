try:
    result = 10 / x
except Exception as e:
    print("DEBUG:", e.__class__.__name__, "-", e)
