# Write a program to check whether an inputted number is Peterson or not

def is_peterson_number(n):
    digits = list(map(int, str(n)))
    num_digits = len(digits)
    peterson_sum = sum(factorial(digit) for digit in digits)

    return peterson_sum == n


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is Peterson
if is_peterson_number(number):
    print(f"{number} is a Peterson number.")
else:
    print(f"{number} is not a Peterson number.")
