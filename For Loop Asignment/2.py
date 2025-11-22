#Write a program to print the multiplication table of n, where n is entered by  the user using for loop
print("--------------------------------------------------------------------------------")
print("\t\t\tMultiplication Table")
print("--------------------------------------------------------------------------------")
n=int(input("Enter a number: "))
for i in range(1, 11):
    print("\t\t\t", n, "x", i, "=", n*i)
