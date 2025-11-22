#WAP to check whether a number is palindrome or not
'''141--->141'''
n=int(input("Enter a number: "))
x=n
s=0
while n>0:
    rem=n%10
    s=s*10+rem
    n=n//10
if s==x:
    print(f"{x} is a Palindrome no")
else:
    print(f"{x} is Not a Palindrome no")