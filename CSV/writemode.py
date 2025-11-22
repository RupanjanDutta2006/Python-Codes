import csv
data=[
    ['Name','Class','Section'],
    ['Rupa',12,'A'],
    ['Rup',12,'A'],
    ['Rohit',11,'B']
]
print(data)
x=input("Enter the File  = ")
with open(x,mode='w',newline='') as file:
    p=csv.writer(file)
    p.writerows(data)
print("File Created Sucessfully!!!")