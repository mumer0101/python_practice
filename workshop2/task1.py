def calculate(do, a, b):
    if do == "add":
        return a + b
    elif do == "subtract":
        return a - b
    elif do == "multiply":
        return a * b
    elif do == "divide":
        return a / b
    
print(calculate("add", 10, 5))
print(calculate("subtract", 10, 5))
print(calculate("multiply", 10, 5))
print(calculate("divide", 10, 5))

