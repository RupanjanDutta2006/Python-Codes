#WAP to print the content of the file 
x=input("Enter the File Name = ")
r=open("D:/Python/Pranab Sir 1/File Handling/"+x,"r")
print(r.read())
r.close()