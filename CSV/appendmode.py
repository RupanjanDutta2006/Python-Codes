import csv
data=[
    ['Roll no','Name','Total'],
    [1,'Rupanjan',400],
    [2,'Ankita',340],
    [3,'Susmita',400]
]
x=input("Enter the File name = ")
with open(x,mode='a',newline='') as file:
    add=csv.writer(file)
    add.writerows(data)
print("File updated sucessfully!!!")