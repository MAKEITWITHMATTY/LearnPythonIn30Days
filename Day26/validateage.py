def validate_age(age):
    print("Incoming age:", age, type(age))
    if age > 18:
        print("Compared age > 18")
        return "Adult"
    elif age > 12:
        print("Compared age > 12")
        return "Teen"
    else:
        print("Fallback: Child")
        return "Child"


print(validate_age("20"))
