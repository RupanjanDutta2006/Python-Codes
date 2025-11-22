#duplicate list copy
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
for i in range(0,n,1):
    if li[i] not in li2 and li.count(li[i])>1:
        li2.append(li[i])
print(li2)