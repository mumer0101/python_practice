# task5operations.py

def calculate(do, a, b):
    if do == "add":
        return a + b
    elif do == "subtract":
        return a - b
    elif do == "multiply":
        return a * b
    elif do == "divide":
        return a / b

def calculate_sum(*args):
    total = sum(args)
    print(f"The sum is: {total}")
    return total
