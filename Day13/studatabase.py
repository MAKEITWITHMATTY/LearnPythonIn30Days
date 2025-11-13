students = [
    {"name": "Alice", "id": 101, "grades": [85, 90, 92]},
    {"name": "Bob", "id": 102, "grades": [78, 82, 88]},
    {"name": "Charlie", "id": 103, "grades": [92, 95, 97]},
]

for student in students:
    print(f"\n{student['name']} (ID: {student['id']})")
    average = sum(student["grades"]) / len(student["grades"])
    print(f"Grades: {student['grades']}")
    print(f"Average: {round(average, 2)}")
