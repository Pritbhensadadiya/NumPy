import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([6,7,8,9,])

new_arr1 = np.vstack((arr1,arr2))
print(new_arr1)
print("\n")
new_arr2 = np.hstack((arr1,arr2))
print(new_arr2)
