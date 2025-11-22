#Write a program to calculate the sum of series 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2 using for loop
n = int(input("Enter the Range: "))
s = 0
for i in range(1, n + 1):
    if i == n:
        print("1/", i, "^2 = ", end=' ')
        s += 1 / (i ** 2)
    else:
        print("1/", i, "^2 + ", end=' ')
        s += 1 / (i ** 2)
print(s)