''' Write a python program to display powers of a number without using formatting character.'''
x = int(input("Enter a number: "))
y=int(input("Enter the power: "))
for i in range(1, y+1):
    print(x**i)