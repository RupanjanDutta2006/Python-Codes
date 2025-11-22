#WAP to print the series 1,4,9,16,25
n = int(input("Enter the Range: "))
print("The series is: ", end="")
for i in range(1, n+1):
    print(i**2, end=" ")