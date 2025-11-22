#WAP to check whether a no is prime or not(Method 2)
n = int(input("Enter a number: "))
c=0
i=1
x=n
while i <= n // 2:
    if n % i == 0:
        c += 1
    i += 1
if c == 1:
    print(f"{x} is a Prime no")
else:
    print(f"{x} is Not a Prime no")