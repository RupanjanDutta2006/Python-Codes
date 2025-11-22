'''Write a python program to concatenate two strings sing + operator,append a string using += 
operator, repeat a string using * operator.
'''
#concatenate operation
x=input("Enter first string: ")
y=input("Enter second string: ")
z=x+y
print("Concatenated string is:",z)
#Append operation
z+=y
print("Appended string is:",z)
#Repeat operation
a=int(input("Enter number of times to repeat the string: "))
print("Repeated string is:",z*a)