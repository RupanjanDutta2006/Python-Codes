#WAP to check whether a no is Disarium number or not
x = int(input("Enter a number: "))
n=x;c=0;temp=x;s=0
while temp > 0:
    c += 1
    temp = temp // 10
temp=n
while temp > 0:
    rem = temp % 10
    s = s + (rem ** c)
    temp = temp // 10
    c=c-1
if s == x:
    print(f"{x} is a Disarium number")
else:
    print(f"{x} is not a Disarium number")