#WAP to print multiplication table of a number
n=int(input("Enter a number = "))
print("--------------------------------------------------")
print("\t\tMultiplication Table")
print("--------------------------------------------------")
for i in range(1, 11):
    print("\t\t",n,"*",i,"=",n*i)