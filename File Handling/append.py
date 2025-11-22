p=open("D:/Python/Pranab Sir 1/File Handling/pratima.txt","a")
p.write("\nAmi sir next cls e valo na korle barite case deben.")
p.close()
p=open("D:/Python/Pranab Sir 1/File Handling/pratima.txt","r")
for i in p.readlines():
    print(i,end='')
print(p.read())
p.close()