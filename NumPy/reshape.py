### 4. Reshape a NumPy Array
import numpy as np
li=[]
n=int(input("Enter the range = "))

for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
# Create a one-dimensional NumPy array
array = np.array(li)
print("Original Array:", array)
x=int(input("Enter the no of Rows = "))
reshaped_array = array.reshape(x,n//x)
print("Reshaped Array:\n", reshaped_array)