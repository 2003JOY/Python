# Write a function to sort a list of numbers. Use this function in a program to sort floating point numbers.

# Function to sort numbers
def sort_numbers(numbers, ascending=True):
    sorted_numbers = sorted(numbers, reverse=not ascending)
    return sorted_numbers


# Get input from the user
numbers = []
num_count = int(input("Enter the number of floating-point numbers: "))

# Collect the numbers
for i in range(num_count):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

# Sort the numbers in ascending order
sorted_numbers = sort_numbers(numbers)

# Display the sorted numbers
print("Sorted numbers in ascending order:")
for number in sorted_numbers:
    print(number)

# Sort the numbers in descending order
sorted_numbers = sort_numbers(numbers, ascending=False)

# Display the sorted numbers
print("Sorted numbers in descending order:")
for number in sorted_numbers:
    print(number)
