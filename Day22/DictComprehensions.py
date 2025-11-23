names = ["Matty", "Alice", "Bob"]
name_lengths = {name: len(name) for name in names}
print(names)
print(name_lengths)

text = "banana"
freq = {char: text.count(char) for char in set(text)}
print(freq)
