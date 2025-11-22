#Write a program to classify a given number as prime or composite using for loop.
n=int(input("Enter a number: "))
f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    print(n,"is a prime number.")
else:
    print(n,"is a composite number.")