#WAP to print sod of a no. by using return type
def sod(n,s=0):   # keyword argument  & default argument
    while(n>0):
        rem=n%10
        s=s+rem
        n=n//10
    return s
n=int(input("Enter the No. = "))
#x=sod(n)  # calling as keyword parameter
#print("Sum of Digit = ",x)
print("Sum of Digit = ",sod(n))  # calling