# Write a program to generate calendar of a month given the start_day and the number of days in that month using for loop
sd = int(input("Enter the start day (1-7, where 1 is Monday): "))
nd = int(input("Enter the number of days in the month: "))

# Print the calendar header
print("Mo Tu We Th Fr Sa Su")

# Print leading spaces for the first week
for i in range(1, sd):
    print("   ", end='')

# Print the days of the month
for day in range(1, nd + 1):
    print(f"{day:2}", end=' ')
    if (day + sd - 1) % 7 == 0:
        print()
