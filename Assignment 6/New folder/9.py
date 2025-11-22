'''Write a python program hat finds whether a given character is present in a string or not.In case it is 
present it prints the index at which it is present. Do not use built in function to search the key.
'''
x=input("Enter the String = ")
y=input("Enter the Character to be searched for = ")
f=0
for i in range(0,len(x),1):
    if x[i]==y:
        print("Character found at index:",i)
        f=1
        break
if f==0:
    print("Character not found.")