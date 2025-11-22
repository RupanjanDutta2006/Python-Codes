#WAP to check whether a No is Krishnamurti or not
n = int(input("Enter a number: "))
x = n
s = 0
f=1
while n>0:
    rem = n % 10
    f=1
    for i in range(1, rem + 1):
        f=f*i
    s = s + f
    n = n // 10
if s == x:
    print(f"{x} is a Krishnamurti number")
else:
    print(f"{x} is not a Krishnamurti number")