#WAP to check greatest between 3 no
a=int(input("Enter the 1st no = "))
b=int(input("Enter the 2nd no = "))
c=int(input("Enter the 3rd no = "))
if a==b and a>c:
    print("1st and 2nd no are equal and",a,"is greater than",c)
elif a==b and a<c:
    print("1st and 2nd no are equal and",c,"is greater than",a)
elif b==c and a>c:
    print("2nd and 3rd no are equal and",a,"is greater than",c)
elif b==c and a<c:
    print("2nd and 3rd no are equal and",c,"is greater than",a)
elif a==c and b>c:
    print("1st and 3rd no are equal and",b,"is greater than",c)
elif a==c and b<c:
    print("1st and 3rd no are equal and",c,"is greater than",b)
elif a>b and a>c:
    print(a,"is the greatest no than the rest ones")
elif b>c and b>a:
    print(b,"is the greatest no than the rest ones")
elif c>a and c>b:
    print(c,"is the greatest no than the rest ones")
else:
    print("The 3 no are equal to each other")

