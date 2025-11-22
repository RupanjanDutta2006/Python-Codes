# Write a program to calculate the value of an investment using for loop.Input an initial value of investment and annual interest, and calculate the value of investment over time.
i=int(input("Enter the initial investment amount: "))
r=int(input("Enter the annual interest rate (in %): "))
t=int(input("Enter the number of years: "))
for j in range(1, t + 1):
    i += i * r / 100
print("The value of the investment after", t, "years is:", i)