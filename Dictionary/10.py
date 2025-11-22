x=int(input("Enter the No = "))
n=x;i=1;s=' ';c=0
while x>0:
    rem=x%2
    r=str(rem)
    s=r+s
    if rem==1:
        c=c+1
    x=x//2
if c%2==0:
    print(n,"is a Evil no ")
else:
    print(n,"is not a Evil no")