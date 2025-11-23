words = ["logic", "LED", "python", "pedal", "loop", "resistor"]
target = "l"

highlighted = [w.upper() if target in w.lower() else w for w in words]

print(highlighted)
