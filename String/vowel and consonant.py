#WAP to print the Vowels and Consonants in a string
s=input("Enter the string: ")
for i in s:
    if i in 'aeiouAEIOU':
        print(i, end=' ')
    else:
        print(i, end=' ')