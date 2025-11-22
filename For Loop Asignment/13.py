# Write a program to calculate the sum of cubes of numbers from 1 - n using for loop.
n = int(input("Enter the Range: "))
s = 0
for i in range(1, n + 1):
    if i == n:
        print(i, " ^ 3 /", i, " = ", end=' ')
        s += (i ** 3) / i
    else:
        print(i, " ^ 3 /", i, " + ", end=' ')
        s += (i ** 3) / i
print(s)