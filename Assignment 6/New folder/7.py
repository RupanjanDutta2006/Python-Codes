'''Write a python program that encrypts a message by adding a key value to every character.(Caesar 
Cipher).[Hints: Say ,if key=3,then add 3 to every character]'''
x=input("Enter a message to encrypt: ")
k=int(input("Enter the key value (numeric): "))
print("Encrypted message: ", end="")
for i in range(len(x)):
    print(chr(ord(x[i]) + k), end="")
    