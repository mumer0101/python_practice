def log_decorator(func):
    def wrapper(*args, **kwargs):  
        result = func(*args, **kwargs)
        
        print(f"Operation: {args[0]}")
        print(f"Operands: {args[1]}, {args[2]}")
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
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
