def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))

def show_menu():
    print("Temperature Converter")
    print("---------------------")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")

def main():
    show_menu()
    choice = input("Choose an option (1-6): ")

    temp = float(input("Enter the temperature: "))

    if choice == "1":
        print(c_to_f(temp))
    elif choice == "2":
        print(f_to_c(temp))
    elif choice == "3":
        print(c_to_k(temp))
    elif choice == "4":
        print(k_to_c(temp))
    elif choice == "5":
        print(f_to_k(temp))
    elif choice == "6":
        print(k_to_f(temp))
    else:
        print("Invalid choice.")

main()
