#Write a program to calculate the sum of series 1 + 1/2 + 1/3+……+ 1/n using for loop
n=int(input("Enter the Range: "))
s=0
for i in range(1, n + 1):
    if i==n:
        print("1/", i, " = ",end=' ')
        s += 1 / i
    else:
        print("1/", i, " + ", end=' ')
        s += 1 / i
print(s)