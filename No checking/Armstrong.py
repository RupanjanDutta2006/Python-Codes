#WAP to check whether a no is Armstrong or not
n = int(input("Enter a number: "))
x=n;s=0;c=0
while n > 0:
    c=c+1
    rem = n % 10
n=x
while n > 0:
    rem = n % 10
    p=pow(rem, c)
    s = s + p
    n = n // 10
if s == x:
    print(f"{x} is an Armstrong number")
else:
    print(f"{x} is not an Armstrong number")