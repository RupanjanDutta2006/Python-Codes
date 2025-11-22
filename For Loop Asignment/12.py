#Write a program to calculate the sum of series 1^2/1 + 2^2/2 + 3^2/3 + ... + n^2/n using for loop
n = int(input("Enter the Range: "))
s = 0
for i in range(1, n + 1):
    if i == n:
        print(i, " ^ 2 /", i, " = ", end=' ')
        s=s+(i**2)/i
    else:
        print(i, " ^ 2 /", i, " + ", end=' ')
        s += (i**2)/i
print(s)