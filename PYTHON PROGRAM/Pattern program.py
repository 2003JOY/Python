#Write a program to print for n number of lines
#   1
#  010
# 10101
#0101010
#……
#……..

# Program to print 0-010-01010 

n = int(input("Enter number of lines of pattern: "))

for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(1,2*i):
        print((k+1)%2, end="")
    print()