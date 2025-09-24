def show_arg(func):
    def wrapper(*args, **kwargs):
        print("The given arguments are:")
        print(*args)   
        return func(*args, **kwargs)
    return wrapper

@show_arg
def calculate_sum(*args):
    total = sum(args)
    print(f"The sum is: {total}")
    return total

calculate_sum(1, 2, 3)
calculate_sum(10, 20, 30, 40)
