n = int(input("Enter a number: "))
x = n  # Store original number
s = 0
while True:
    s = 0
    
    while n > 0:
        rem = n % 10
        s = s + rem
        n = n // 10
    if s > 9:
        n = s
        continue# Continue with new sum
    else:
        break

if s == 1:
    print(f"{x} is a Magic number")
else:
    print(f"{x} is not a Magic number")
