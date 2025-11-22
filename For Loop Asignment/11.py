#Write a program to calculate the sum of series 1/2 + 2/3 +……+ n/(n+1) using for loop..
n = int(input("Enter the Range: "))
s = 0
for i in range(1, n + 1):
    if i == n:
        print(i, "/", i + 1, " = ", end=' ')
        s += i / (i + 1)
    else:
        print(i, "/", i + 1, " + ", end=' ')
        s += i / (i + 1)
print(s)