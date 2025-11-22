'''Write a program using while loop to read the numbers until -1 is encountered. 
And using for loop also count the number of prime numbers and composite 
numbers entered by the user'''
n = 0
while True:
    n = int(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    c=0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n, "is a prime number.")
    else:
        print(n, "is a composite number.")