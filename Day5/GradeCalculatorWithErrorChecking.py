score = int(input("Enter your test score (0-100): "))

if score > 100 or score < 0:
    print("Error: Please enter a score between 0 and 100.")
else:
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
