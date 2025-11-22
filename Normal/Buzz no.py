#WAP to check whether a no is Buzz or not
n=int(input("Enter the No = "))
if n%7==0 and n%10==0:
    print(n,"is a Buzz Number")
else:
    print(n,"is not a Buzz Number")