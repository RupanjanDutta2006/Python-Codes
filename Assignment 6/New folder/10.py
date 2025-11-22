''' Write a python program that counts the occurrences of a character in a string. Do not use built in 
function .'''

x=input("Enter the String = ")
y=input("Enter the Character to be searched for = ")
count=0
for i in range(0,len(x),1):
    if x[i]==y:
        count+=1
print("Character found", count, "times.")