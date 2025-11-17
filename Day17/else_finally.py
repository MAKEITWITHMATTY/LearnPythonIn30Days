file_name = "data.txt"

try:
    f = open(file_name, "r")
except FileNotFoundError:
    print("No data file found.")
else:
    print("File opened successfully.")
    print("First line:", f.readline())
    f.close()
finally:
    print("Done trying to read the file.")
