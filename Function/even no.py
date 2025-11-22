#WAP to store even no. within a list by using filter func.
def evenodd(li):
    if li%2==0:
        return True
n=int(input("Enter the Range = "))
li=[]
evenli=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
evenli=filter(evenodd,li)   #positional parameter
for i in evenli:
    print(i,end=',')