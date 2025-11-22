#WAP to print the series 3,31,312,3123,31234
n = int(input("Enter the Range: "))
a=3
print("The series is: 3", end="")
for i in range(1,n+1,1):
    j=i
    s=(a*10)+j
    print(s, end=", ")
    j+=1
    a=s