# Write a program to find the prime factors of a number.

def find_prime_factors(number):
    prime_factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return prime_factors

# Test the function
input_number = int(input("Enter a number: "))
result = find_prime_factors(input_number)
print("Prime factors:", result)

