#Write a program to calculate the average of first n natural numbers using for loop
n=int(input("Enter a natural number: "))
sum=0
for i in range(1,n+1):
    sum+=i
average=sum/n
print("The average of first",n,"natural numbers is:",average)