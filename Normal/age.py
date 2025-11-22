#WAP to check the age
a=int(input("Enter your age = "))
if a>0 and a<=12:
    print("You are a Child")
elif a>12 and a<=19:
    print("You are a Teenager")
elif a>19 and a<=35:
    print("You are a Young Adult")
elif a>35 and a<=60:
    print("You are an Adult")
elif a>60 and a<=100:
    print("You are a Senior Citizen")
elif a>100:
    print("Invalid age")
else:
    print("Age cannot be negative")