#WAP to check whether a no is Spy number or not
n = int(input("Enter a number: "))
x=n;s=0;p=1
while n > 0:
    rem = n % 10
    s = s + rem
    p = p * rem
    n = n // 10
if s == p:
    print(f"{x} is a Spy number")
else:
    print(f"{x} is not a Spy number")