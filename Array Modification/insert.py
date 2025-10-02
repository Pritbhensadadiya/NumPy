"""
np.insert(array , index,values,axisnone)
"""
import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_array = np.insert(arr,2,100,axis=0)
print(new_array)

