N = int(input("Enter a number:"))

if N <= 0:
    print("Error: Enter a number greater than 0")

elif N == 1:
    print(0)

else:
    Fibonacci_no = [0, 1]
    while len(Fibonacci_no) < N:
        Fibonacci_no.append(Fibonacci_no[-1] + Fibonacci_no[-2])
    print(Fibonacci_no)
