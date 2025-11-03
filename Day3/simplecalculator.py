print("Simple Calculator")
print("------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

if op == "+":
    print(f"Result: {num1 + num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operator!")
