import csv
# Read CSV file
x=input("Enter the File name = ")
with open(x,mode='r') as file:
    a=csv.reader(file)
    header=next(a)
    print(header)
    for i in a:
        print(i)