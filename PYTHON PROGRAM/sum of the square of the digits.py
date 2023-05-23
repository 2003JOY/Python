#Write a program to find the sum of the square of the digits of any given positive integer.

print("Enter a Number: ")
num = int(input())

sum = 0
while num!=0:
    rem = num%10
    sqr = rem*rem
    sum = sum+sqr
    num = int(num/10)

print("\nSum of squares of digits of given number is: ")
print(sum)