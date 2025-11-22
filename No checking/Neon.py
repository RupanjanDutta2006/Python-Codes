#WAP to check whether a no is Neon number or not
n = int(input("Enter a number: "))
x=n*n
s=0
while x > 0:
    rem = x % 10
    s = s + rem
    x = x // 10
if s == n:
    print(f"{n} is a Neon number")
else:
    print(f"{n} is not a Neon number")