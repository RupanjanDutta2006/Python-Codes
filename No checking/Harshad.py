#WAP to check whether a no is Harshad number or not
x = int(input("Enter a number: "))
s=0;n=x
while n > 0:
    rem = n % 10
    s = s + rem
    n = n // 10
if x % s == 0:
    print(f"{x} is a Harshad number")
else:
    print(f"{x} is not a Harshad number")