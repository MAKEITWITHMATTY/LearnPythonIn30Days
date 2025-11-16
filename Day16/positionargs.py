def greet(name, age):
    print(f"Hello {name}, age {age}")

greet("Matty", 32)   # works
greet(32, "Matty")   # totally wrong order

greet(name="Matty", age=32)
greet(age=32, name="Matty")   # also works
