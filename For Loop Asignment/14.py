# Write a program to calculate the sum of squares of even numbers using for loop.
n = int(input("Enter the Range: "))
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        if i == n:
            print(i, " ^ 2 = ", end=' ')
            s += i ** 2
        else:
            print(i, " ^ 2 + ", end=' ')
            s += i ** 2
print(s)