#WAP to store positive & negative list in 2 separate list
def check(li):  # keyword argument
    for i in li:
        if i>0:
            posli.append(i)
        elif i<0:
            negli.append(i)
    print("Positive element's list = ",posli,"\nNegative element's list = ",negli)
n=int(input("Enter the Range = "))
li=[]
posli=[]
negli=[]
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print(li)
check(li)  # keyword parameter  [10,-50,30,-40,50]