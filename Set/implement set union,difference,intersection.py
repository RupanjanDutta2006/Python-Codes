#WAP To implement set union, difference and intersection
set1=set()
set2=set()
set3=set()
n=int(input("Enter the number of elements in set 1: "))
for i in range(n):
    e=int(input("Enter element: "))
    set1.add(e)

m=int(input("Enter the number of elements in set 2: "))
for i in range(m):
    e=int(input("Enter element: "))
    set2.add(e)
print("Set 1:", set1)
print("Set 2:", set2)
#Set Union
set3=set1|set2
print("Set Union:", set3)
#Set Intersection
set4=set1&set2
print("Set Intersection:", set4)
#Set Difference
set5=set1-set2
print("Set Difference(set1-set2):", set5)
print("Set Difference(set2-set1):", set2-set1)