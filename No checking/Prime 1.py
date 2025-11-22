#WAP to check whether a no is prime or not(Method 1)
n=int(input("Enter a number: "))
c=0
i=1
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    print(f"{n} is a Prime no")
else:
    print(f"{n} is Not a Prime no")