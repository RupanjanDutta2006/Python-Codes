#WAP to implement a tuple runtime
t1=()
n=int(input("Enter the number of elements in the tuple: "))
for i in range(n):
    x=int(input("Enter the No: "))
    t1+= (x,)
print(t1)
for i in t1:
    print(i)
x=input("Enter a string =")
t1=tuple(x.split(' '))
print(t1)