"""
reshape(rows,column) specify the new shape
if dimention match
"""


import numpy as np

arr = np.array([10,20,30,40,50,60])
reshape_Arr = arr.reshape(2,3)
print(reshape_Arr)
