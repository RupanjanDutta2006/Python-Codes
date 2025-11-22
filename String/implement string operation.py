#WAP to implement string operation
'''
 0 1 2 3 4 5 6 7-->forward traversing
 R u p a n j a n
-8-7-6-5-4-3-2-1<---backward traversing
'''
x=input("Enter the string = ")
print(x[0:3])
print(x[:2])
print(x[::1])
print(x[::-1])
print(x[1:8:2])
print(x[-1:-8:-2])