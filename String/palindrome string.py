#WAP to check if a string is a palindrome or not
x=input("Enter the string: ")
if x==x[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
