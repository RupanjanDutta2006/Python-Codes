#WAP to calc. factorial of a no. 
def fact(n,f=1):  #default argument
    for i in range(1,n+1,1):
        f=f*i
    print("Factorial of ",n,"is =",f)
n=int(input("Enter the No. = "))
fact(n)  #calling with positional parameter
n=int(input("Enter the No. = "))
fact(n)  #calling with positional parameter
n=int(input("Enter the No. = "))
fact(n)  #calling with positional parameter