#WAP to convert seconds to hours
sec=int(input("Enter the Seconds = "))
hr=sec//3600
sec=sec%3600
min=sec//60
sec=sec%60
print("Hours =",hr,"Minutes =",min,"Seconds =",sec)