import json

# --- JSON string coming from somewhere (API, network, embedded text) ---
json_text = '{"score": 1200, "active": true, "items": ["sword", "shield"]}'

# Convert JSON string → Python dictionary
data = json.loads(json_text)

print("Python data:")
print(data)
print(type(data))   # Should be <class 'dict'>

# Modify the data (just to show it's normal Python)
data["score"] += 300
data["active"] = False
data["items"].append("health potion")

# Convert Python dictionary → JSON string
json_string = json.dumps(data)

print("\nBack to JSON string:")
print(json_string)
print(type(json_string))   # Should be <class 'str'>
