#WAP to print the fibonacci series
n = int(input("Enter the Range: "))
a=0;b=1
print("The Fibonacci series is: ",a,b, end=" ")
for i in range(1,n-1,1):
    s=a+b
    print(s, end=" ")
    a=b
    b=s
