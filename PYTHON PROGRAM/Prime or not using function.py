#Define a function to check whether a number is prime or not. Write a program to show the use of this function

num=int(input("Enter a number: "))
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return ("This number is not prime")
    return ("This number is a prime")
print(isprime(num))