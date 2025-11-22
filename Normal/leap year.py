#WAP to check whether a year is leap year or not
yr=int(input("Enter the Year = "))
if yr%400==0:
    print(yr,"is a leap year")
elif yr%4==0 and yr%100!=0:
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")