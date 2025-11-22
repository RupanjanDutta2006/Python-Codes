#WAP to create email id
import random as r
x=input("Enter the first name=").lower()
for i in range(len(x)):
    if x[i]==" ":
        x=x[:i]
        break
y=input("Enter the last name=").lower()
for i in range(len(y)):
    if y[i]==" ":
        y=y[:i]
        break
z=input("Enter the domain name=").lower()
for i in range(len(z)):
    if z[i]==" ":
        z=z[:i]
        break
if z=="gmail" or z=="yahoo" or z=="outlook":
    s=x+y
    n=str(r.randint(100,999))
    w=s+n+"@"+z+".com"
    print("Email id is:", w)
else:
    print("Invalid domain name.Not possible to create email id.")