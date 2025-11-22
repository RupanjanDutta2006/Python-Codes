#WAP to calc. factorial of a no. by using recursion
def fact(x):   #positional argument
    if x==1:
        return 1
    else:
        return x*fact(x-1)   #tail recursion
n=int(input("Enter the No. = "))
if n==0 or n==1:
    print("Factorial = 1")
elif n<0:
    print("-ve no. factorial can't be possible")
else:
    print(fact(n))  # positional parameter