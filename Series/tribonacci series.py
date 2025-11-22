#WAP to print the Tribonacci series
n = int(input("Enter the Range: "))
a=0;b=0;c=1
s=0
print("The Tribonacci series is: ", end="")
for i in range(1,n-2,1):
    s=a+b+c
    print(s, end=" ")
    a=b
    b=c
    c=s