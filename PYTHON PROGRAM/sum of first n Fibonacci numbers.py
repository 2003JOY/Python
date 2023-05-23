# Write a program to find the sum of first n Fibonacci numbers

def sum_of_fibonacci(n):
    if n <= 0:
        return 0

    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    sum_fib = 1  # Initialize the sum to 1 (since we have the first Fibonacci number already)

    for i in range(2, n):
        fib_num = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(fib_num)
        sum_fib += fib_num

    return sum_fib

# Test the function
input_n = int(input("Enter the value of n: "))
result = sum_of_fibonacci(input_n)
print("Sum of the first", input_n, "Fibonacci numbers:", result)