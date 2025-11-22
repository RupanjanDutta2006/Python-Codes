#Write a program to print all the numbers from m-n thereby classify them as even or odd using for loop.
m=int(input("Enter the starting number (m): "))
n=int(input("Enter the ending number (n): "))
for i in range(m, n+1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")