li=[]
x=int(input("Enter the range of the list = "))
for i in range(0,x ,1):
    li.append(int(input("Enter the No = ")))
print("list = ",li)
z=int(input("Enter the index to be inserted ="))
li.insert(z,(int(input("Enter the no = "))))
del(li[z+1])
print("Modified list  =",li)