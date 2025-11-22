#WAP to check whether a no is duck number or not(Method 1)
n = input("Enter a number: ")
if '0' in n[1:]:
    print(f"{n} is a Duck number")
else:
    print(f"{n} is not a Duck number")
#WAP to check whether a no is duck number or not(Method 2)
n = input("Enter a number: ")
f=0;x=n
if n[0] == '0':
    print(f"{x} is not a Duck number")
else:
    for i in range(1,len(x),1):
        if x[i] == '0':
            f = 1
            break
    if f == 1:
        print(f"{x} is a Duck number")
    else:
        print(f"{x} is not a Duck number")