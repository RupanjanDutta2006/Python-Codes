import csv
li=[]
heading=[]
a=int(input("Enter the No of Column = "))
for i in range(0,a,1):
   b=input(f"Enter the Head line for {i} index = ")
   b=b.capitalize()
   heading.append(b)
print(heading)
r=int(input("Enter the no of ROWS = "))
for i in range(0,r,1):
    row=[]
    for j in range(0,a,1):
        c=input(f"Enter the value for {1} No Student , Column {heading[j]} = ")
        c=c.capitalize()
        row.append(c)
    li.append(row)
print(li)
x=input("Enter the File name = ")
with open(x, mode='w', newline='\n') as file:
    data_x = csv.writer(file)
    data_x.writerow(heading)
    data_x.writerows(li)
print("File Created Successfully!!!")