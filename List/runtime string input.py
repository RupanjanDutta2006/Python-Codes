#WAP take runtime string input and print the list and sort it
li = []
n = int(input("Enter number of elements in the list: "))
for i in range(0,n,1):
    y=input("Enter element: ")
    li.append(y)
print(li)
li.sort()
print("Sorted list:", li)