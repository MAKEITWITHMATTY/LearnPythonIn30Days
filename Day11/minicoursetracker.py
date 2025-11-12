available_courses = ("Math", "Science", "History", "Art")
my_courses = {"Math", "Art"}

print("All courses:", available_courses)
print("My courses:", my_courses)

remaining = set(available_courses) - my_courses
print("Still available:", remaining)
