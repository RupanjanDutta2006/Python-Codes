#WAP to print the series 2, 4, 6, 8, 10
n=int(input("Enter the Range: "))
print("The series is: ", end="")
for i in range(1, n+1, 1):
    if i % 2 == 0:
       print(i, end=" ")