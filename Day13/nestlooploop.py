numbers = [
    {"id": 1, "label": "One", "facts": ["Odd", "First natural number"]},
    {"id": 2, "label": "Two", "facts": ["Even", "Only even prime number"]},
    {"id": 3, "label": "Three", "facts": ["Odd", "Triangular number"]},
]

for num in numbers:
    print(f"\nID: {num['id']} → {num['label']}")
    print("Facts:")
    for fact in num["facts"]:
        print(f"  - {fact}")
