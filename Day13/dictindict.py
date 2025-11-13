contacts = {
    "Matty": {"email": "matty@example.com", "phone": "123-456"},
    "Alex": {"email": "alex@example.com", "phone": "987-654"},
}

for name, info in contacts.items():
    print(f"\n{name}")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
