#Matrix multiplication 
import numpy as np
x=int(input("Enter the Range For both Matrix= "))
li1=[]
li2=[]
for i in range(0,x,1):
    y1=int(input("Enter the NO for 1st Matrix= "))
    li1.append(y1)
for i in range(0,x,1):
    y2=int(input("Enter the NO for 2nd Matrix= "))
    li2.append(y2)
array1=np.array(li1)
array2=np.array(li2)
a=int(input("Enter the Row no for 1st array and also the Column no for 2nd list = "))
r_array1=array1.reshape(a,x//a)
print("1st Matrix = \n",r_array1)
r_array2=array2.reshape(x//a,a)
print("2nd Matrix = \n",r_array2)
p_matrix=np.dot(r_array1,r_array2)
print("Product matrix = \n",p_matrix)