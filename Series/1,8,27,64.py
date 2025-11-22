#WAP to print the series 1, 8, 27, 64
n = int(input("Enter the Range: "))
print("The series is: ", end="")
for i in range(1, n+1):
    print(i**3, end=" ")