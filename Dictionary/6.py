x={}
w=int(input("Enter the range of the Dictionary = "))
for i in range(1,w+1,1):
    y=int(input("Enter the key = "))
    x[y]=int(input("Enter the Value = "))
print("The Dictionary will be = ",x)
z=int(input("Enter the Key to be appended = "))

x.update({z:int(input("Enter the value for the append - "))})
print("The updated dictionary will be  =",x)