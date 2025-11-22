#WAP to check whether a no is prime or not(Method 3)
n = int(input("Enter a number: "))
f=0
i=1
while i<n:
    if n%i==0:
        f=1
        break
    i+=1
if f==0:
    print(f"{n} is a Prime no")
else:
    print(f"{n} is Not a Prime no")