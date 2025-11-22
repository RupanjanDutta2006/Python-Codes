import numpy as np
arr = np.array([9, 7, 8,10, 2,3])
x = np.searchsorted(np.sort(arr), 10)    #2,3,7,8,9,10
print(x)
#right
arr = np.array([6, 9, 8, 7])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5,7])
x = np.searchsorted(arr, [2, 4, 6,8])
print(x)