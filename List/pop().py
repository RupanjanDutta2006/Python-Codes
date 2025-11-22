#WAP to implement pop()
n=int(input("Enter the Range = "))
li=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
li.pop()
print(li)
y=int(input("Enter the index to pop element from: "))
li.pop(y)
print(li)