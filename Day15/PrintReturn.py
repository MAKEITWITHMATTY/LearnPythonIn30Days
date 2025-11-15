def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(2, 3)   # prints 5, but you cannot use the value
x = add_return(2, 3)
print(x * 10)     # 50
