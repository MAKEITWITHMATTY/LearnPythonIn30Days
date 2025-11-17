def get_float(prompt):
    """Ask the user for a floating-point number, with ValueError handling."""
    while True:
        text = input(prompt)
        try:
            value = float(text)
            return value
        except ValueError:
            print("Please enter a number (you can use decimals like 21.5).")


def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def log_conversion(celsius, fahrenheit, file_name="temp_log.txt"):
    """Append the conversion to a log file."""
    try:
        with open(file_name, "a") as f:
            f.write(f"{celsius} C -> {fahrenheit} F\n")
    except FileNotFoundError:
        # This is rare for "a" mode, but we’ll be explicit anyway
        print(f"Could not find '{file_name}'. Creating new file.")
        with open(file_name, "w") as f:
            f.write(f"{celsius} C -> {fahrenheit} F\n")


def main():
    print("=== Temperature Converter (Celsius → Fahrenheit) ===")
    c = get_float("Enter temperature in °C: ")
    f = c_to_f(c)
    print(f"{c}°C is {f}°F")

    log_conversion(c, f)
    print("Conversion logged to temp_log.txt")


if __name__ == "__main__":
    main()
