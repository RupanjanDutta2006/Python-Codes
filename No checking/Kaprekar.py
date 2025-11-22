#WAP to check whether a no is Kaprekar number or not
n = int(input("Enter a number: "))
x=n;c=0;s=0
while n > 0:
    c = c + 1
    n = n // 10
sq=n*n
p=pow(10, c)
a=sq%p
b=sq//p
if a + b == x:
    print(f"{x} is a Kaprekar number")
else:
    print(f"{x} is not a Kaprekar number")